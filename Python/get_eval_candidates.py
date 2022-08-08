# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_eval_candidates.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkauppi <jkauppi@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/06 12:08:10 by jkauppi           #+#    #+#              #
#    Updated: 2022/08/08 14:45:07 by jkauppi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
from Utils import *
from Users import *

def analyze_error(response):
	if response["error"] == "Not authorized" and response["message"] == "The access token expired":
		print("Get new token!")

def print_projects(project_data_list):
		print("Number of projects: {}".format(len(project_data_list)))
		for project_data_table in project_data_list:
			print("Project id: {}. Name: {}".format(project_data_table["id"], project_data_table["name"]))

def print_project_users(project_users_data_list):
		print("Number of users in project: {}".format(len(project_users_data_list)))
		for project_user_data_table in project_users_data_list:
#			print("Project id: {}. Name: {}".format(project_user_data_table["id"], project_user_data_table["name"]))
			for param_name in project_user_data_table:
				print("  {} = {}".format(param_name, project_user_data_table[param_name]))
			print("\n\n")

def get_project_users_data(token, project_id):
	response_data = []
	url = 'https://api.intra.42.fr/v2/projects/' + str(project_id) + "/projects_users"
	headers = {"Authorization": "Bearer {}".format(token)}
	loop_cnt = 1
	params = {"page": loop_cnt}
	response = get_data_from_42api(url, headers, params)
	while type(response) == list and len(response) > 0:
		print("Loop: {}".format(loop_cnt))
		print_project_users(response)
		response_data.extend(response)
		loop_cnt += 1
		params = {"page": loop_cnt}
		response = get_data_from_42api(url, headers, params)
#	for project_users_data_table in response_data:
	#	print("Project name: {} ({})".format(project_users_data_table["name"], project_users_data_table["slug"]))
#		for param_name in project_users_data_table:
#			print("  {} = {}".format(param_name, project_users_data_table[param_name]))
#		print("\n\n")
	return ()

def get_project_data(token, project_id):
	response_data = []
	url = 'https://api.intra.42.fr/v2/projects/' + str(project_id)
	headers = {"Authorization": "Bearer {}".format(token)}
	params = {}
	response = get_data_from_42api(url, headers, params)
	response_data.append(response)
	project_data_table = response_data[0]
	print("Project name: {} ({})".format(project_data_table["name"], project_data_table["slug"]))
	for param_name in project_data_table:
		print("  {} = {}".format(param_name, project_data_table[param_name]))
	print("\n\n")
	print("Token is valid")
	return ()

def get_projects_data(token):
	response_data = []
	url = 'https://api.intra.42.fr/v2/projects/'
	headers = {"Authorization": "Bearer {}".format(token)}
	loop_cnt = 1
	params = {"page": loop_cnt}
	response = utils.getDataFrom42Api(url, headers, params)
	while type(response) == list and len(response) > 0:
		print("Loop: {}".format(loop_cnt))
		print_projects(response)
		response_data.extend(response)
		loop_cnt += 1
		params = {"page": loop_cnt}
		response = get_data_from_42api(url, headers, params)
	if type(response) == dict:
		analyze_error(response)
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
	utils = Utils()
	token = utils.getToken()
	# get_users_data(token)
	# get_campus_data(token)
	# get_cursus_data(token)
	# get_projects_data(token)
	# get_project_data(token, 1081)
	# get_project_users_data(token, 1081)
	users = Users(utils)
	# users.getAllUsers()
	# users.getUser(1081)
	users.getUser(25980)


# Project name: First Internship (first-internship)
#   id = 118

# Project id: 1081. Name: DSLR



# campus = [
# {'id': 51, 'name': 'Berlin', 'time_zone': 'Europe/Berlin', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-04T13:33:03.279Z'}, 'users_count': 154, 'vogsphere_id': 48, 'country': 'Germany', 'address': 'Harzer Strasse 39', 'zip': '12059', 'city': 'Berlin', 'website': 'http://42berlin.de/', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42berlin.de', 'default_hidden_phone': False},
# {'id': 54, 'name': '42-test', 'time_zone': 'Europe/Paris', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-08-03T09:00:16.774Z'}, 'users_count': 10, 'vogsphere_id': 47, 'country': 'France', 'address': '96 Bd Bessières', 'zip': '75017', 'city': 'Paris', 'website': 'http://42paris.fr', 'facebook': '', 'twitter': '', 'active': True, 'public': False, 'email_extension': '42paris.fr', 'default_hidden_phone': False},
# {'id': 55, 'name': 'Tétouan', 'time_zone': 'Africa/Casablanca', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-07-28T21:02:55.617Z'}, 'users_count': 340, 'vogsphere_id': 44, 'country': 'Morocco', 'address': 'Parc Tétouan Shore, CP93150 , Martil, Tétouan', 'zip': '93000', 'city': 'Tétouan', 'website': 'https://1337.ma', 'facebook': '', 'twitter': 'https://twitter.com/1337FIL', 'active': True, 'public': True, 'email_extension': '1337.ma', 'default_hidden_phone': False},
# {'id': 52, 'name': 'Florence', 'time_zone': 'Europe/Rome', 'language': {'id': 16, 'name': 'Italian', 'identifier': 'it', 'created_at': '2020-03-12T13:30:39.859Z', 'updated_at': '2022-07-28T13:54:29.498Z'}, 'users_count': 305, 'vogsphere_id': 46, 'country': 'Italy', 'address': 'Via del Tiratoio, 1', 'zip': '50124', 'city': 'Firenze', 'website': 'https://www.42firenze.it', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42firenze.it', 'default_hidden_phone': True}, {'id': 46, 'name': 'Barcelona', 'time_zone': 'Europe/Madrid', 'language': {'id': 11, 'name': 'Spanish', 'identifier': 'es', 'created_at': '2019-08-09T15:14:32.544Z', 'updated_at': '2022-08-05T16:34:20.062Z'}, 'users_count': 809, 'vogsphere_id': 38, 'country': 'Spain', 'address': 'Parc Tecnològic de Barcelona Activa, Carrer Albert Einstein', 'zip': '08042', 'city': 'Barcelona', 'website': 'https://www.42barcelona.com', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42barcelona.com', 'default_hidden_phone': True}, {'id': 32, 'name': 'Yerevan', 'time_zone': 'Asia/Yerevan', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-04T13:33:03.279Z'}, 'users_count': 1222, 'vogsphere_id': 22, 'country': 'Armenia', 'address': '16 Halabyan St', 'zip': '0038', 'city': 'Yerevan', 'website': 'https://42yerevan.am/', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42yerevan.am', 'default_hidden_phone': False}, {'id': 49, 'name': 'Istanbul', 'time_zone': 'Europe/Istanbul', 'language': {'id': 18, 'name': 'Turkish', 'identifier': 'tr', 'created_at': '2021-08-20T10:50:01.782Z', 'updated_at': '2022-08-03T11:59:08.948Z'}, 'users_count': 1398, 'vogsphere_id': 36, 'country': 'Turkey', 'address': 'Ayazağa Mah. Azerbaycan Cad. Vadistanbul İş Blokları 2B Blok Kat 3 Sarıyer', 'zip': '34000', 'city': 'Istanbul', 'website': 'http://www.42istanbul.com.tr', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42istanbul.com.tr', 'default_hidden_phone': False}, {'id': 50, 'name': 'Kocaeli', 'time_zone': 'Europe/Istanbul', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-01T03:11:37.371Z'}, 'users_count': 836, 'vogsphere_id': 37, 'country': 'Turkey', 'address': '- No address yet -', 'zip': '41000', 'city': 'Kocaeli', 'website': 'http://www.42kocaeli.com.tr', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42kocaeli.com.tr', 'default_hidden_phone': False}, {'id': 47, 'name': 'Lausanne', 'time_zone': 'Europe/Zurich', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-08-03T11:58:41.836Z'}, 'users_count': 619, 'vogsphere_id': 35, 'country': 'Switzerland', 'address': '64 Rue de Lausanne', 'zip': '1020', 'city': 'Renens', 'website': 'https://42lausanne.ch/', 'facebook': 'https://www.facebook.com/42Lausanne', 'twitter': 'https://twitter.com/42lausanne', 'active': True, 'public': True, 'email_extension': '42lausanne.ch', 'default_hidden_phone': True}, {'id': 44, 'name': 'Wolfsburg', 'time_zone': 'Europe/Berlin', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-07-28T13:54:20.054Z'}, 'users_count': 1867, 'vogsphere_id': 29, 'country': 'Germany', 'address': 'Porschestraße 2c', 'zip': '38440', 'city': 'Wolfsburg', 'website': 'http://42wolfsburg.de/', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42wolfsburg.de', 'default_hidden_phone': False}, {'id': 40, 'name': 'Urduliz', 'time_zone': 'Europe/Madrid', 'language': {'id': 11, 'name': 'Spanish', 'identifier': 'es', 'created_at': '2019-08-09T15:14:32.544Z', 'updated_at': '2022-07-28T13:54:32.548Z'}, 'users_count': 577, 'vogsphere_id': 32, 'country': 'Spain', 'address': 'Aita Gotzon Kalea 37', 'zip': '48610', 'city': 'Urduliz', 'website': 'https://42urduliz.com/', 'facebook': '', 'twitter': 'https://twitter.com/42UrdulizFTef', 'active': True, 'public': True, 'email_extension': '42urduliz.com', 'default_hidden_phone': True}, {'id': 33, 'name': 'Bangkok', 'time_zone': 'Asia/Bangkok', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-07-28T13:54:20.054Z'}, 'users_count': 1123, 'vogsphere_id': 31, 'country': 'Thailand', 'address': '1 Thanon Chalong Krung, Lat Krabang', 'zip': '10520', 'city': 'Bangkok', 'website': 'https://www.42bangkok.com/', 'facebook': 'https://www.facebook.com/42Bangkok/', 'twitter': 'https://twitter.com/42bangkok', 'active': True, 'public': True, 'email_extension': '42bangkok.com', 'default_hidden_phone': False}, {'id': 25, 'name': 'Quebec', 'time_zone': 'America/New_York', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-07-28T21:02:55.617Z'}, 'users_count': 318, 'vogsphere_id': 27, 'country': 'Canada', 'address': '330, St-Vallier Est, bureau 300', 'zip': 'G1K 9C5', 'city': 'Québec', 'website': '42quebec.com', 'facebook': 'https://www.facebook.com/42quebec/', 'twitter': 'https://twitter.com/42_quebec', 'active': True, 'public': True, 'email_extension': '42quebec.com', 'default_hidden_phone': True}, {'id': 15, 'name': 'Cape-Town', 'time_zone': 'Africa/Johannesburg', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-07-28T13:54:20.054Z'}, 'users_count': 845, 'vogsphere_id': 12, 'country': 'South Africa', 'address': 'Portswood, Workshop17, Dock Rd, V & A Waterfront', 'zip': '8002', 'city': 'Cape-Town', 'website': 'https://www.wethinkcode.co.za/', 'facebook': 'https://www.facebook.com/wethinkcode/', 'twitter': 'https://twitter.com/wethinkcode', 'active': False, 'public': False, 'email_extension': 'wethinkcode.co.za', 'default_hidden_phone': False}, {'id': 43, 'name': 'Abu Dhabi', 'time_zone': 'Asia/Dubai', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-04T10:43:29.312Z'}, 'users_count': 1106, 'vogsphere_id': 30, 'country': 'United Arab Emirates', 'address': 'Mina Zayed, Warehouse District ', 'zip': '00000', 'city': 'Abu Dhabi', 'website': 'https://42abudhabi.ae/', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42abudhabi.ae', 'default_hidden_phone': False}, {'id': 42, 'name': '42Network', 'time_zone': 'Europe/Paris', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-07-28T13:54:20.054Z'}, 'users_count': 186, 'vogsphere_id': 43, 'country': 'France', 'address': '96 boulevard Bessières', 'zip': '75017', 'city': 'PARIS', 'website': 'http://42network.org/', 'facebook': '', 'twitter': '', 'active': True, 'public': False, 'email_extension': '42network.org', 'default_hidden_phone': False}, {'id': 38, 'name': 'Lisboa', 'time_zone': 'Europe/Lisbon', 'language': {'id': 9, 'name': 'Portuguese', 'identifier': 'pt', 'created_at': '2019-01-29T15:17:48.227Z', 'updated_at': '2022-08-01T17:22:07.600Z'}, 'users_count': 1406, 'vogsphere_id': 25, 'country': 'Portugal', 'address': 'Rua Neves Ferreira, 13B', 'zip': '1170-273', 'city': 'Lisboa', 'website': 'http://www.42lisboa.com', 'facebook': 'https://www.facebook.com/42-Lisboa-100970235020298/', 'twitter': 'https://twitter.com/42lisboa', 'active': True, 'public': True, 'email_extension': '42lisboa.com', 'default_hidden_phone': False}, {'id': 28, 'name': 'Rio de Janeiro', 'time_zone': 'America/Sao_Paulo', 'language': {'id': 9, 'name': 'Portuguese', 'identifier': 'pt', 'created_at': '2019-01-29T15:17:48.227Z', 'updated_at': '2022-07-28T13:54:26.270Z'}, 'users_count': 669, 'vogsphere_id': 40, 'country': 'Brazil', 'address': 'Via Binario do Porto, 299 / 4th floor', 'zip': '20000-000', 'city': 'Rio de Janeiro', 'website': 'https://42.rio', 'facebook': '', 'twitter': '@Escola42Rio', 'active': True, 'public': True, 'email_extension': '42.rio', 'default_hidden_phone': False}, {'id': 23, 'name': 'Kazan', 'time_zone': 'Europe/Moscow', 'language': {'id': 6, 'name': 'Russian', 'identifier': 'ru', 'created_at': '2018-06-08T10:49:26.608Z', 'updated_at': '2018-06-08T10:49:26.608Z'}, 'users_count': 3818, 'vogsphere_id': 18, 'country': 'Russian Federation', 'address': 'Spartakovskaya, 2b2', 'zip': '420000', 'city': 'Kazan', 'website': '21-school.ru', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '21-school.ru', 'default_hidden_phone': False}, {'id': 29, 'name': 'Seoul', 'time_zone': 'Asia/Seoul', 'language': {'id': 14, 'name': 'Korean', 'identifier': 'ko', 'created_at': '2020-01-08T10:56:47.481Z', 'updated_at': '2022-07-28T13:54:37.540Z'}, 'users_count': 4271, 'vogsphere_id': 19, 'country': 'Korea, Republic of', 'address': 'Gaepo Digital Innovation Park, 416, Gaepo-ro, Gangnam-gu,', 'zip': '000000', 'city': 'Seoul', 'website': 'https://www.42seoul.kr', 'facebook': 'https://www.facebook.com/inno.aca/  ', 'twitter': 'https://twitter.com/inno_aca', 'active': True, 'public': True, 'email_extension': '42seoul.kr', 'default_hidden_phone': False}, {'id': 20, 'name': 'São-Paulo', 'time_zone': 'America/Sao_Paulo', 'language': {'id': 17, 'name': 'Brazilian Portuguese', 'identifier': 'pt_br', 'created_at': '2020-12-10T14:15:00.994Z', 'updated_at': '2022-07-28T13:54:44.527Z'}, 'users_count': 2653, 'vogsphere_id': 14, 'country': 'Brazil', 'address': 'Rua Aspicuelta, 422, cj. 71A', 'zip': '05433-010', 'city': 'São Paulo', 'website': 'https://42sp.org.br', 'facebook': '', 'twitter': '', 'active': True, 'public': True, 'email_extension': '42sp.org.br', 'default_hidden_phone': False}, {'id': 26, 'name': 'Tokyo', 'time_zone': 'Asia/Tokyo', 'language': {'id': 13, 'name': 'Japanese', 'identifier': 'ja', 'created_at': '2019-11-15T13:34:10.581Z', 'updated_at': '2022-08-04T20:28:09.771Z'}, 'users_count': 4274, 'vogsphere_id': 17, 'country': 'Japan', 'address': 'Sumitomo Fudosan Roppongi Grand Tower 3-2-1 Roppongi Minato-ku reception: 24F', 'zip': '106-6224', 'city': 'Tokyo', 'website': 'https://42tokyo.jp', 'facebook': 'https://www.facebook.com/42tokyo/', 'twitter': 'https://twitter.com/42_tokyo', 'active': True, 'public': True, 'email_extension': '42tokyo.jp', 'default_hidden_phone': True}, {'id': 13, 'name': 'Helsinki', 'time_zone': 'Europe/Helsinki', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-03T11:58:37.155Z'}, 'users_count': 1165, 'vogsphere_id': 13, 'country': 'Finland', 'address': 'Haapaniemenkatu 5', 'zip': '00530', 'city': 'Helsinki', 'website': 'https://www.hive.fi/', 'facebook': 'https://www.facebook.com/HiveHelsinki', 'twitter': 'https://twitter.com/hivehelsinki', 'active': True, 'public': True, 'email_extension': 'hive.fi', 'default_hidden_phone': False}, {'id': 22, 'name': 'Madrid', 'time_zone': 'Europe/Madrid', 'language': {'id': 11, 'name': 'Spanish', 'identifier': 'es', 'created_at': '2019-08-09T15:14:32.544Z', 'updated_at': '2022-08-02T07:37:09.256Z'}, 'users_count': 3001, 'vogsphere_id': 15, 'country': 'Spain', 'address': 'Distrito Telefónica - Edificio Norte 3, Ronda de la Comunicación, s/n', 'zip': '28050', 'city': 'Madrid', 'website': 'http://www.42madrid.com/', 'facebook': 'https://facebook.com/fundaciontef', 'twitter': 'https://twitter.com/42MadridFTef', 'active': True, 'public': True, 'email_extension': '42madrid.com', 'default_hidden_phone': True}, {'id': 21, 'name': 'Benguerir', 'time_zone': 'Africa/Casablanca', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-08-03T09:02:11.338Z'}, 'users_count': 1862, 'vogsphere_id': 11, 'country': 'Morocco', 'address': 'Lot 660, Hay Moulay Rachid, Ben Guerir 43150', 'zip': '43150', 'city': 'Benguerir', 'website': 'https://1337.ma', 'facebook': 'https://www.facebook.com/1337FutureIsLoading', 'twitter': 'https://twitter.com/1337FIL', 'active': True, 'public': True, 'email_extension': '1337.ma', 'default_hidden_phone': False}, {'id': 14, 'name': 'Amsterdam', 'time_zone': 'Europe/Amsterdam', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-03T13:12:49.572Z'}, 'users_count': 1824, 'vogsphere_id': 8, 'country': 'Netherlands', 'address': 'Kattenburgerstraat 7', 'zip': '1018 JA', 'city': 'Amsterdam', 'website': 'http://www.codam.nl', 'facebook': 'https://www.facebook.com/codamcodingcollege/', 'twitter': 'https://twitter.com/CodamCollege', 'active': True, 'public': True, 'email_extension': 'codam.nl', 'default_hidden_phone': False}, {'id': 17, 'name': 'Moscow', 'time_zone': 'Europe/Moscow', 'language': {'id': 6, 'name': 'Russian', 'identifier': 'ru', 'created_at': '2018-06-08T10:49:26.608Z', 'updated_at': '2018-06-08T10:49:26.608Z'}, 'users_count': 8780, 'vogsphere_id': 7, 'country': 'Russian Federation', 'address': 'Vyatskaya 27, business park "Factoria"', 'zip': '127015', 'city': 'Moscow', 'website': '21-school.ru', 'facebook': 'https://www.facebook.com/21coding', 'twitter': 'https://twitter.com/21coding', 'active': True, 'public': True, 'email_extension': '21-school.ru', 'default_hidden_phone': False}, {'id': 9, 'name': 'Lyon', 'time_zone': 'Europe/Paris', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-07-31T06:56:32.976Z'}, 'users_count': 2398, 'vogsphere_id': 4, 'country': 'France', 'address': 'Campus Région – 78 route de Paris', 'zip': '69260', 'city': 'Charbonnières-les-Bains', 'website': 'https://www.42lyon.fr/', 'facebook': 'https://www.facebook.com/42lyon', 'twitter': 'https://twitter.com/42lyon', 'active': True, 'public': True, 'email_extension': '42lyon.fr', 'default_hidden_phone': False}, {'id': 7, 'name': 'Fremont', 'time_zone': 'America/Tijuana', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-07-28T13:54:20.054Z'}, 'users_count': 18214, 'vogsphere_id': 2, 'country': 'United States', 'address': '6 600 Dumbarton Circle', 'zip': '94555', 'city': 'Fremont', 'website': 'https://www.42.us.org/', 'facebook': 'https://www.facebook.com/42SiliconValley', 'twitter': 'https://twitter.com/42SiliconValley', 'active': False, 'public': False, 'email_extension': '42.us.org', 'default_hidden_phone': False}, {'id': 12, 'name': 'Brussels', 'time_zone': 'Europe/Brussels', 'language': {'id': 2, 'name': 'English', 'identifier': 'en', 'created_at': '2015-04-14T16:07:38.122Z', 'updated_at': '2022-08-01T14:42:05.156Z'}, 'users_count': 1640, 'vogsphere_id': 5, 'country': 'Belgium', 'address': 'Cantersteen 10/12', 'zip': '1000', 'city': 'Brussels', 'website': 'https://www.s19.be', 'facebook': 'https://www.facebook.com/19network42/', 'twitter': 'https://twitter.com/19network42/', 'active': True, 'public': True, 'email_extension': 's19.be', 'default_hidden_phone': False}, {'id': 16, 'name': 'Khouribga', 'time_zone': 'Africa/Casablanca', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-08-02T07:37:07.969Z'}, 'users_count': 2626, 'vogsphere_id': 6, 'country': 'Morocco', 'address': 'Mail Central', 'zip': '25000', 'city': 'Khouribga', 'website': 'https://1337.ma', 'facebook': '', 'twitter': 'https://twitter.com/1337FIL', 'active': True, 'public': True, 'email_extension': '1337.ma', 'default_hidden_phone': False}, {'id': 8, 'name': 'Kyiv', 'time_zone': 'Europe/Kiev', 'language': {'id': 5, 'name': 'Ukrainian', 'identifier': 'uk', 'created_at': '2016-08-21T11:42:57.272Z', 'updated_at': '2022-01-15T02:43:00.045Z'}, 'users_count': 2637, 'vogsphere_id': None, 'country': 'Ukraine', 'address': 'Dorohozhytska St, 3', 'zip': '04119', 'city': 'Kyiv', 'website': 'https://unit.ua/', 'facebook': 'https://www.facebook.com/unit.factory/', 'twitter': '', 'active': False, 'public': False, 'email_extension': 'unit.ua', 'default_hidden_phone': False}, {'id': 1, 'name': 'Paris', 'time_zone': 'Europe/Paris', 'language': {'id': 1, 'name': 'Français', 'identifier': 'fr', 'created_at': '2014-11-02T16:43:38.466Z', 'updated_at': '2022-08-05T16:34:11.325Z'}, 'users_count': 24149, 'vogsphere_id': 1, 'country': 'France', 'address': '96, boulevard Bessières', 'zip': '75017', 'city': 'Paris', 'website': 'http://www.42.fr/', 'facebook': 'https://facebook.com/42born2code', 'twitter': 'https://twitter.com/42born2code', 'active': True, 'public': True, 'email_extension': '42.fr', 'default_hidden_phone': False}]




#  user = {'id': 59720, 'email': 'jkauppi@student.hive.fi', 'login': 'jkauppi', 'first_name': 'Juhani', 'last_name': 'Kauppi', 'usual_full_name': 'Juhani Kauppi', 'usual_first_name': None, 'url': 'https://api.intra.42.fr/v2/users/jkauppi', 'phone': 'hidden', 'displayname': 'Juhani Kauppi', 'image_url': 'https://cdn.intra.42.fr/users/jkauppi.jpg', 'new_image_url': 'https://profile.intra.42.fr/users/jkauppi/photo', 'staff?': False, 'correction_point': 13, 'pool_month': 'july', 'pool_year': '2019', 'location': 'c3r1p3', 'wallet': 285, 'anonymize_date': '2025-08-06T00:00:00.000+03:00', 'data_erasure_date': '2025-08-06T00:00:00.000+03:00', 'created_at': '2019-07-02T12:00:02.059Z', 'updated_at': '2022-08-07T08:05:07.729Z', 'alumnized_at': None, 'alumni?': False}

#   teams = [{'id': 3751806, 'name': 'Jussi', 'url': 'https://api.intra.42.fr/v2/teams/3751806', 'final_mark': 0, 'project_id': 1081, 'created_at': '2021-08-27T14:19:57.309Z', 'updated_at': '2021-10-19T12:21:58.565Z', 'status': 'finished', 'terminating_at': None, 'users': [{'id': 59720, 'login': 'jkauppi', 'url': 'https://api.intra.42.fr/v2/users/jkauppi', 'leader': True, 'occurrence': 0, 'validated': True, 'projects_user_id': 2314121}], 'locked?': True, 'validated?': False, 'closed?': True, 'repo_url': 'git@vogsphere-v2.hive.fi:vogsphere/intra-uuid-f6de09ac-589c-409d-a01c-f707a66059b1-3751806', 'repo_uuid': 'intra-uuid-f6de09ac-589c-409d-a01c-f707a66059b1-3751806', 'locked_at': '2021-08-27T14:20:07.536Z', 'closed_at': '2021-10-19T10:18:29.703Z', 'project_session_id': 6584, 'project_gitlab_path': None}, {'id': 3851968, 'name': "jkauppi's team", 'url': 'https://api.intra.42.fr/v2/teams/3851968', 'final_mark': 125, 'project_id': 1081, 'created_at': '2021-10-22T12:42:18.675Z', 'updated_at': '2021-10-29T09:57:38.373Z', 'status': 'finished', 'terminating_at': None, 'users': [{'id': 59720, 'login': 'jkauppi', 'url': 'https://api.intra.42.fr/v2/users/jkauppi', 'leader': True, 'occurrence': 1, 'validated': True, 'projects_user_id': 2314121}], 'locked?': True, 'validated?': True, 'closed?': True, 'repo_url': 'git@vogsphere-v2.hive.fi:vogsphere/intra-uuid-6a2cd3d9-12de-4200-a672-2f486ab595f4-3851968', 'repo_uuid': 'intra-uuid-6a2cd3d9-12de-4200-a672-2f486ab595f4-3851968', 'locked_at': '2021-10-22T12:42:31.019Z', 'closed_at': '2021-10-27T10:40:31.403Z', 'project_session_id': 6584, 'project_gitlab_path': None}]
