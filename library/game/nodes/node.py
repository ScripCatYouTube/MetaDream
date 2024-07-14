from .nodes import Nodes
from .random_sha import get_name_file

class Node:
	def __init__(self, parent = 'root'):
		self.id = get_name_file(end = '')
		self.type_node = Nodes.Node.value
		self.parent = parent

	def get_source(self):
		return {
					'id': self.id,
					'type': self.type_node,
					'parent': self.parent
		}