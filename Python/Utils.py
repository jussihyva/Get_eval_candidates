import os
import requests
import time
import json

class Utils():
	def __init__(self) -> None:
		self.token = None

	def __getClientId(self):
		file = open("{}/{}".format(os.environ["HOME"], ".ssh/hive_api_client_id"))
		clientId = file.readline().strip()
		return (clientId)

	def __getClientSecret(self):
		file = open("{}/{}".format(os.environ["HOME"], ".ssh/hive_api_client_secret"))
		clientSecret = file.readline().strip()
		return (clientSecret)

	def __getToken(self):
		print("Get new token!")
		clientId = self.__getClientId()
		clientSecret = self.__getClientSecret()
		url = "https://api.intra.42.fr/oauth/token"
		data = {
			"grant_type": "client_credentials",
			"client_id": "{}".format(clientId),
			"client_secret": "{}".format(clientSecret)}
		response = requests.post(url, data = data).json()
		print(data)
		print(response)
		token = response["access_token"]
		return (token)

	def getToken(self):
		if self.token == None:
			self.token = self.__getToken()
		return (self.token)

	def readDataFrom42Api(self, url, headers, params):
		status_code = 0
		while status_code != 200:
			response = requests.get(url, headers = headers, params = params)
			status_code = response.status_code
			if status_code == 429:
				print("Wait 20 sec. Reason: {}".format(response.text))
				time.sleep(20)
			else:
				response = json.loads(response.text)
		print("Number of users: {}".format(type(response)))
		return (response)
