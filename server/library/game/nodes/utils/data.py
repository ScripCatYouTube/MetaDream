import urllib3
import requests

from PIL import Image
from io import BytesIO

class Data:
	def __init__(self, string_data: str, format_convert: str = 'png') -> None:
		self.data = self.update_data(string_data)
		self.format = format_convert


	def update_data(self, string_data: str) -> dict:
		bin_data: bytes = None
		extension: str = None

		if string_data[:8] == 'https://' or string_data[:7] == 'http://': 
			bin_data = self.url_data(string_data)

		elif isinstance(string_data, Image):
			bin_data = self.pillow_image(string_data)
			extension = self.format

		else:
			try:
				with open(string_data, 'rb') as f: 
					bin_data = [i for i in f.read()]

			except (FileNotFoundError):
				pass

		try:
			if bin_data and extension == None:
				bin_data = str(bin_data)[2:][:-1] 
				extension = string_data.split('.')[-1]

		except (AttributeError, ValueError, TypeError): pass

		return {'data': bin_data, 'type': 'raw', 'type_file': extension}


	def url_data(self, url) -> bytes:
		try:
			return requests.get(url).content

		except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError, urllib3.exceptions.NameResolutionError): 
			pass


	def pillow_image(self, image) -> bytes:
		with BytesIO() as f:
			image.save(f, format = self.format.upper())
			return f.getvalue()		
