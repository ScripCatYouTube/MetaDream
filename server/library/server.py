from flask import session
from datetime import datetime
from json import loads, JSONDecodeError
from importlib.machinery import SourceFileLoader


from .list_users import ListUsers
from .thread_loop import ThreadLoop
from .game.nodes.utils.data import Data
from .authorization import Authorization
from .message_tracker import MessageTracker
from .game.control_locations import ControlLocations

class Server:
	def __init__(self, icon, path_user = './', path_server = './', path_data = './usr_dat', path_user_data = './usr_dat/users/'):
		self.app = None
		self.player_count = 0
		self.path_user = path_user
		self.path_server = path_server
		self.path_data = path_data
		self.path_user_data = path_user_data

		self.ping_data = {"players": self.player_count, "icon": Data(icon).data, 'utc': datetime.now().astimezone().isoformat().split('+')[1]}

		self.players = ListUsers()
		self.thread_loop = ThreadLoop(self)
		self.msg_tracker = MessageTracker()
		self.user_class = self.import_user()
		self.server_class = self.import_server()
		self.autho = Authorization(self.path_user_data, self)
		self.control_locations = ControlLocations()


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
		server_class =  SourceFileLoader("server_module", self.path_server).load_module().Server
		self.dev_server = server_class(self)
		return server_class


	def get_user(self):
		if session.get('user'):
			return self.players.get_user(session['user'])


	def response_update(self, resp):
		if 'response' in resp:
			if resp['response'] == 'update_user_class':
				if self.get_user().data.check_values('permissions', 'admin', 'creator'):

					self.user_class = self.import_user()
					return {'status': True, 'data': 'Successfuly re-imported'}

				return {'status': False, 'data': 'You\'re is\'nt admin/creator'}


			elif resp['response'] == 'update_server_class':
				if self.get_user().data.check_values('permissions', 'admin', 'creator'):

					self.server_class = self.import_server()
					return {'status': True, 'data': 'Successfuly re-imported'}

				return {'status': False, 'data': 'You\'re is\'nt admin/creator'}


