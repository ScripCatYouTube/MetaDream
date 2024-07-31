from .nodes import Nodes
from .node2d import Node2D
from library.game.nodes.utils.data import Data


class Texture2D(Node2D):
	def __init__(self, texture, position = [0, 0], rotation = 0, scale = [0, 0], parent = 'root'):
		super().__init__(parent, position = position, rotation = rotation, scale = scale, parent = parent)
		self.type_node = Nodes.Texture2D.value
		self.texture = Data(texture)

	def get_node(self) -> dict:
		return {
					'id': self.id,
					'parent': self.parent,
					'type': self.type_node,
					'texture': self.texture.data
		}
