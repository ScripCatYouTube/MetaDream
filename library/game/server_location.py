from .nodes import 
from .location import Location

class ServerLocation(Location):
	def __init__(self, server) -> None:
		self.server = server
		self.players = {} # 'player': Node2D

		super().__init__()


	def camera_rect(self, rect) -> list:
		objects = []

		for i in self.object:
			node = self.object[i].rect

			if rect.is_collision(node):
				objects += node.get_source()

		return objects


	def camera_player(self, player_name: str) -> list:
		return self.camera_rect(
			self.players[player_name].rect
		)


	def view_player(self, player_name: str) -> dict:
		
	
	#def add_node(self, node) -> dict:

