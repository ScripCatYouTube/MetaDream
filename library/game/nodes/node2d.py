from .node import Node
from .nodes import Nodes

class Node2D(Node):
	def __init__(self, parent = 'root'):
		super().__init__(parent)
		self.type_node = Nodes.Node2D.value
		self.parent = parent

	def get_source(self):
		return {
					'id': self.id,
					'type': self.type_node,
					'parent': self.parent
		}