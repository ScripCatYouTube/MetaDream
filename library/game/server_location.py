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


	def camera_player(self, player_name) -> list:
		return self.camera_rect(
			self.players[player_name].rect
		)
