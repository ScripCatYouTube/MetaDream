from flask import session

from .user_data import UserData
from .fabric_user import FabricUser 


class Authorization:
	def __init__(self, path_user_data, server):
		self.path_user_data = path_user_data
		self.server = server


	def is_have_user(self, username, password):
		usr_data = UserData(self.path_user_data)

		return usr_data.find_file({'username': username, 'password': password}, is_create = False)


	def is_have_login(self, username):
		usr_data = UserData(self.path_user_data)

		return usr_data.find_file({'username': username}, is_create = False)


	def login(self, username, password):
		if self.is_have_user(username, password) == False: return {'status': False, 'data': f'Doesn\'t registred account'}

		self.create_user(username, password)
		return {'status': True, 'data': 'Successful loggined'}


	def register(self, username, password):
		if self.is_have_login(username): return {'status': False, 'data': 'With this nickname has account'}
		#usr_data = UserData(self.path_user_data)

		#usr_data.find_file({'username': username, 'password': password}, is_create = False)
		self.create_user(username, password)
		return {'status': True, 'data': 'Successful registred'}


	def logout(self):
		is_session_popped = False
		is_list_popped = False

		if self.logout_list_user(): is_list_popped = True
		if self.logout_session(): is_session_popped = True

		return {'status': is_list_popped or is_session_popped, 'session_pop': is_session_popped, 'players_pop': is_list_popped}


	def logout_list_user(self):
		if session.get('user'):
			self.server.players.delete_hash(session['user'])

			return True


	def logout_session(self):
		if session.get('user'):
			session.pop('user', None)

			return True


	def create_user(self, username, password): 
		usr = FabricUser(self.server, {'username': username, 'password': password, 'admin': False, 'creator': False})

		self.server.players.add_user(usr)
		#session['user']
