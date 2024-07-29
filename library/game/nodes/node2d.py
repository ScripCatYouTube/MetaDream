from .rect import Rect
from .node import Node
from .nodes import Nodes

class Node2D(Node):
	def __init__(self, position = [0, 0], rotation = 0, scale = [0, 0], parent = 'root'):
		super().__init__(parent)
		self.parent = parent
		self.rect = Rect(position = position, size = [0, 0], scale = scale, rotation = rotation)
		self.type_node = Nodes.Node2D.value


	def get_node(self) -> dict:
		return {
					'id': self.id,
					'parent': self.parent,
					'type': self.type_node,
		}

	def _get_source(self) -> dict:
		return self.rect.update(self._get_source())

	def get_source(self) -> list:
		return [self.get_node()] + self.get_children()