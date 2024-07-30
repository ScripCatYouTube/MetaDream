from .nodes import Nodes
from library.game.nodes.utils.random_sha import get_name_file


class Node:
	def __init__(self, parent = 'root') -> None:
		self.id = get_name_file(end = '')
		self.type_node = Nodes.Node.value
		self.children = []
		self.parent = parent

		self.parent_init()


	def parent_init(self):
		if isinstance(self.parent, str): return

		elif isinstance(self.parent, Node):
			self.parent = Node.id

		else:
			raise TypeError('Parent can be only type string(hash id) or Node')

	def _get_source(self) -> dict:
		return {
			'id': self.id,
			'type': self.type_node,
			'parent': self.parent

		}


	def get_source(self) -> list:
		return [self._get_source()] + self.get_children()


	def get_children(self) -> list:
		children = []

		for i in self.children:
			children.append(i.get_source())

			if i.children != []:
				children += i.get_children()

		return children