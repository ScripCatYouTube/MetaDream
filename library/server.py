from json import loads
from flask import session
from importlib.machinery import SourceFileLoader

import os

from .game.nodes.data import Data
from .list_users import ListUsers
from .thread_loop import ThreadLoop
from .authorization import Authorization
from .message_tracker import MessageTracker

class Server:
	def __init__(self, icon, path_user = './', path_server = './', path_data = './usr_dat', path_user_data = './usr_dat/'):
		self.app = None
		self.player_count = 0
		self.path_user = path_user
		self.path_server = path_server
		self.path_data = path_data
		self.path_user_data = path_user_data

		self.ping_data = {"players": self.player_count, "icon": Data(icon).data}

		self.players = ListUsers()
		self.thread_loop = ThreadLoop(self)
		self.msg_tracker = MessageTracker()
		self.user_class = self.import_user()
		self.server_class = self.import_server()
		self.autho = Authorization(self.path_user_data, self)

	def _response(self, resp):
		if session.get('user'):
			
			answer_update = self.response_update(resp)
			if answer_update: return answer_update

			return self.get_user().response(resp)

		return {'status': False, 'data': "You are not logged. User class is'nt added to session."}


	def response(self, value):
		try:
			return self._response(loads(value))
		except JSONDecodeError:
			return {'status': False, 'data': 'JSON error load'}


	def import_user(self):
		return SourceFileLoader("user_module", self.path_user).load_module().User

	def import_server(self):
		return SourceFileLoader("server_module", self.path_server).load_module().Server


	def get_user(self):
		if session.get('user'):
			return self.players.get_user(session['user'])

	def response_update(self, response):
		is_admin_creator = self.get_user().data.read(args = ['admin', 'creator']) 

		if 'response' in resp:
			if resp['response'] == 'update_user_class':
				if is_admin_creator['admin'] or is_admin_creator['creator']:

					self.user_class = self.import_user()
					return {'status': True, 'data': 'Successfuly re-imported'}

				return {'status': False, 'data': 'You\'re is\'nt admin/creator'}

			elif resp['response'] == 'update_user_class':
				if is_admin_creator['admin'] or is_admin_creator['creator']:

					self.server_class = self.import_server()
					return {'status': True, 'data': 'Successfuly re-imported'}

				return {'status': False, 'data': 'You\'re is\'nt admin/creator'}		
