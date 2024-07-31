import os
import json

from .game.nodes.utils.random_sha import get_name_file
from .errors import ErrorUserDataFileIsNotExits, ErrorUserDataJsonUnsuccessfulLoad


class UserData:
	def __init__(self, path):
		self.path = path
		self.file = None

		self.create_dirs_if_not_exits()


	def get_files(self):
		return [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]


	def find_file(self, kwargs, is_create = True):
		for i in self.get_files():
			data = self._read(i)
			is_kw = kwargs

			try:
				new_dict = {}
				for ii in kwargs:
					new_dict[ii] = data[ii]
					#print(ii, i, data[ii], kwargs[ii])
					
				if new_dict == kwargs: 
					self.file = i
					return True

			except KeyError: pass

		if is_create: self.create_new_file_data(kwargs)
		
		return False


	def write(self, kwargs, file = None):
		if self.file == None and file == None: raise FileNotFoundError('File is None (0_o)')
		if file == None: file = self.file # if file is None set to registred file(self.file)

		readed_data = self.read(file = file)

		edited_data = readed_data
		for i in kwargs:
			edited_data[i] = kwargs[i]

		self._write(file, edited_data)


	def read(self, file = None, args = []):
		if self.file == None and file == None: raise FileNotFoundError('File is None (0_o)')
		if file == None: file = self.file # if file is None set to registred file(self.file)

		data_readed = {}

		json_data = self._read(file)
			
		for k in json_data:
			try:
				if (args == []) or (k in args):
					data_readed[k] = json_data[k]

			except KeyError:
				data_readed[k] = None
				json_data[k] = None

				self.write({k: None}, file = file)

		return data_readed


	def _write(self, file, data):
		with open(os.path.join(self.path, file), 'w') as f: f.write(json.dumps(data, indent = 4))


	def _read(self, file):
		data = None
		
		try: 
			with open(os.path.join(self.path, file), 'r') as f: data = f.read()
		except FileNotFoundError: 
			raise ErrorUserDataFileIsNotExits(f'Element \'{file}\' isn\'t in directory \'{self.path}\'')

		dict_result = None

		try: 
			dict_result = json.loads(data)
		except json.decoder.JSONDecodeError as e: 
			raise ErrorUserDataJsonUnsuccessfulLoad('JSON Unsuccessful Load. Advanced Information:', e)

		return dict_result


	def create_dirs_if_not_exits(self):
		try: os.makedirs(self.path) # Create directories from self.path
		except FileExistsError: pass # Do nothing if is created 


	def create_new_file_data(self, kwargs):
		name_file = get_name_file()

		self.file = name_file
		self._write(name_file, kwargs)