import urllib3
import requests

class Data:
	def __init__(self, string_data: str) -> None:
		self.data = self.update_data(string_data)


	def update_data(self, string_data: str) -> dict:
		bin_data: bytes = None
		extension: str = None

		if string_data[:8] == 'https://' or string_data[:7] == 'http://': 
			bin_data = self.url_data(string_data)
			extension = 'url'

		else:
			try:
				with open(string_data, 'rb') as f: 
					bin_data = [i for i in f.read()]

			except (FileNotFoundError):
				pass

		try:
			if bin_data and extension != 'url':
				bin_data = str(bin_data)[2:][:-1] 
				extension = string_data.split('.')[-1]

		except (AttributeError, ValueError, TypeError): 
			pass

		return {'data': bin_data, 'type': 'raw', 'type_file': extension}


	def url_data(self, url) -> bytes:
		try:
			return requests.get(url).content

		except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError, urllib3.exceptions.NameResolutionError): 
			pass

			