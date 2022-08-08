class Users():
	def __init__(self, utils) -> None:
		self.utils = utils
		token = self.utils.getToken()
		self.headers = {"Authorization": "Bearer {}".format(token)}

	def __printOne(self, data_table):
		for param_name in data_table:
			print("  {} = {}".format(param_name, data_table[param_name]))

	def __readFullDataFrom42Api(self, url):
		response_data = []
		loop_cnt = 1
		params = {"page": loop_cnt}
		response = self.utils.readDataFrom42Api(url, self.headers, params)
		while type(response) == list and len(response) > 0:
			print("Loop: {}. Number of records: {}".format(loop_cnt, len(response)))
			print("  Only the first record from {} is printed".format(len(response)))
			self.__printOne(response[0])
			response_data.extend(response)
			loop_cnt += 1
			params = {"page": loop_cnt}
			response = self.utils.readDataFrom42Api(url, self.headers, params)
		if type(response) == dict:
			self.utils.analyzeError(response)
		return (response_data)

	def getAllUsers(self):
		url = "ttps://api.intra.42.fr/v2/users"
		userDataList = self.__readFullDataFrom42Api(url)
		return (userDataList)

	def getUser(self, userId):
		url = "https://api.intra.42.fr/v2/users/{}/projects_users".format(userId)
		# url = "https://api.intra.42.fr/v2/projects/{}/projects_users".format(userId)
		userDataList = self.__readFullDataFrom42Api(url)
		return (userDataList)
