from .nodes import Nodes
from .random_sha import get_name_file

class Node:
	def __init__(self, parent = 'root') -> None:
		self.id = get_name_file(end = '')
		self.type_node = Nodes.Node.value
		self.children = []
		self.parent = parent


	def get_source(self) -> list:
		return [{
					'id': self.id,
					'type': self.type_node,
					'parent': self.parent
					
		}] + self.get_children()


	def get_children(self) -> list:
		children = []

		for i in self.children:
			children.append(i.get_source())

			if i.children != []:
				children += i.get_children()

		return children