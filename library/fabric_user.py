from json import dumps, loads
from json.decoder import JSONDecodeError
from datetime import datetime, timedelta

from .user_data import UserData 
from .message_tracker import MessageTracker

class FabricUser:
	def __init__(self, server, kwargs):
		self.server = server
		self.app = server.app
		self.data = UserData(server.path_user_data)
		self.data.find_file(kwargs)
		self.msg_track = MessageTracker()
		self.delta_timedeath = timedelta(minutes = 30) # AFK Time
		self.timedeath = self.delta_timedeath 

		self.update_death_time()

		self.user = server.user_class(self, self.app, self.server, self.data)


	def update_user(self):
		self.user = self.server.user_class(self, self.app, self.server, self.data)


	def response(self, value_dict): 
		#self.update_death_time()
		return self.user.response(value_dict)


	def loop(self):
		self.check_death_time()
		self.user.loop()


	def update_death_time(self):
		self.timedeath = datetime.now() + self.delta_timedeath


	def check_death_time(self):
		if self.timedeath <= datetime.now(): self.server.autho.logout()


	def get_afk_time(self):
		return (self.timedeath - datetime.now()).seconds // 60