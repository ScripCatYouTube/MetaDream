
class User:
	def __init__(self, fabric_user, app, server, vault):
		self.fabuser = fabric_user
		self.app = app
		self.server = server
		self.vault = vault


	def response(self, resp):
		return {'status': True}


	def loop(self):
		pass