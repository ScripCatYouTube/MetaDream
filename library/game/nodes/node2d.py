from .node import Node
from .nodes import Nodes

class Node2D(Node):
	def __init__(self, position = [0, 0], rotation = 0, scale = [0, 0], parent = 'root'):
		super().__init__(parent)
		self.parent = parent
		self.scale = scale
		self.position = position
		self.rotation = rotation
		self.type_node = Nodes.Node2D.value

	def get_source(self):
		return {
					'id': self.id,
					'scale': self.scale,
					'parent': self.parent,
					'type': self.type_node,
					'rotation': self.rotation,
					'position': self.position
		}