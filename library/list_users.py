from flask import session

from library.game.nodes.utils.random_sha import get_name_file

class ListUsers:
	def __init__(self):
		self.users = {}


	def add_user(self, user):
		_hash = get_name_file()

		self.users[_hash] = user
		session['user'] = _hash
		return _hash


	def delete_user(self, user):
		for i in self.users:
			if self.users[i] == user:
				self.users.pop(i)
				return True
		
		return False


	def delete_hash(self, _hash):
		self.users.pop(_hash)


	def get_users(self):
		return list(self.users.values())


	def get_user(self, _hash):
		return self.users[_hash]