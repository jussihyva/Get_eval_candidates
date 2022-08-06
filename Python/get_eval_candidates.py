# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_eval_candidates.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkauppi <jkauppi@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/06 12:08:10 by jkauppi           #+#    #+#              #
#    Updated: 2022/08/06 17:26:23 by jkauppi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import requests
import time
import json

def get_client_id():
	file = open(os.environ["HOME"] + "/.ssh/hive_api_client_id")
	client_id = file.readline().strip()
	return (client_id)

def get_client_secret():
	file = open(os.environ["HOME"] + "/.ssh/hive_api_client_secret")
	client_secret = file.readline().strip()
	return (client_secret)

def get_token(client_id, client_secret):
	print("Get new token!")
	url = "https://api.intra.42.fr/oauth/token"
	data = {
		"grant_type": "client_credentials",
		"client_id": "{}".format(client_id),
		"client_secret": "{}".format(client_secret)}
	response = requests.post(url, data = data).json()
	print(data)
	token = response["access_token"]
	return (token)

def analyze_error(response):
	if response["error"] == "Not authorized" and response["message"] == "The access token expired":
		print("Get new token!")

def print_users(user_data_list):
		print("Number of users: {}".format(len(user_data_list)))
		for user_data_table in user_data_list:
			print("User id: {}".format(user_data_table["id"]))
			for param_name in user_data_table:
				print("  {} = {}".format(param_name, user_data_table[param_name]))
			break

def get_users_data(token):
	response_data = []
	url = 'https://api.intra.42.fr/v2/users'
	headers = {"Authorization": "Bearer {}".format(token)}
	loop_cnt = 1
	params = {"page": loop_cnt}
	response = get_data_from_42api(url, headers, params)
	while type(response) == list and len(response) > 0:
		response_data.extend(response)
		print("Loop: {} ({})".format(loop_cnt, len(response)))
		print_users(response)
		loop_cnt += 1
		params = {"page": loop_cnt}
		response = get_data_from_42api(url, headers, params)
	if type(response) == dict:
		analyze_error(response)
	else:
		print_users(response_data)
		print("Token is valid")
	return ()

def get_projects_data(token):
	response_data = []
	url = 'https://api.intra.42.fr/v2/projects'
	headers = {"Authorization": "Bearer {}".format(token)}
	loop_cnt = 1
	params = {"page": loop_cnt}
	response = get_data_from_42api(url, headers, params)
	while type(response) == list and len(response) > 0:
		print("Loop: {}".format(loop_cnt))
		response_data.extend(response)
		loop_cnt += 1
		params = {"page": loop_cnt}
		response = get_data_from_42api(url, headers, params)
	if type(response) == dict:
		analyze_error(response)
	else:
		for project_data_table in response_data:
			print("Project name: {} ({})".format(project_data_table["name"], project_data_table["slug"]))
			for param_name in project_data_table:
				print("  {} = {}".format(param_name, project_data_table[param_name]))
			print("\n\n")
		print("Token is valid")
	return ()

def get_campus_data(token):
	url = 'https://api.intra.42.fr/v2/campus'
	headers = {"Authorization": "Bearer {}".format(token)}
	response = requests.get(url, headers = headers).json()
	if type(response) == dict:
		analyze_error(response)
	else:
		for campus_data_table in response:
			# print("Project name: {} ({})".format(campus_data_table["name"], campus_data_table["slug"]))
			for param_name in campus_data_table:
				print("  {} = {}".format(param_name, campus_data_table[param_name]))
			print("\n\n")
		print("Token is valid")
	return ()

def get_data_from_42api(url, headers, params):
	status_code = 0
	while status_code != 200:
		response = requests.get(url, headers = headers, params = params)
		status_code = response.status_code
		if status_code == 429:
			time.sleep(20)
		else:
			response = json.loads(response.text)
	print("Number of users: {}".format(type(response)))
	return (response)

def get_cursus_data(token):
	response_data = []
	url = 'https://api.intra.42.fr/v2/cursus'
	headers = {"Authorization": "Bearer {}".format(token)}
	loop_cnt = 1
	params = {"page": loop_cnt}
	response = get_data_from_42api(url, headers, params)
	while type(response) == list and len(response) > 0:
		print("Loop: {}".format(loop_cnt))
		response_data.extend(response)
		loop_cnt += 1
		params = {"page": loop_cnt}
		response = get_data_from_42api(url, headers, params)
	if type(response) == dict:
		analyze_error(response)
	else:
		print("Number of cursus: {}".format(len(response_data)))
		for cursus_data_table in response_data:
			print("DATA: {}".format(cursus_data_table))
			# print("Project name: {} ({})".format(cursus_data_table["name"], cursus_data_table["slug"]))
			for param_name in cursus_data_table:
				print("  {} = {}".format(param_name, cursus_data_table[param_name]))
			print("\n\n")
		print("Token is valid")
	return ()

if __name__ == "__main__":
	client_id = get_client_id()
	client_secret = get_client_secret()
	token = get_token(client_id, client_secret)
	get_users_data(token)
	# get_campus_data(token)
	# get_cursus_data(token)
	# get_projects_data(token)


# Project name: First Internship (first-internship)
#   id = 118
