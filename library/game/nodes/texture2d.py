from .node2d import Node2D
from .data import Data
from .nodes import Nodes

class Texture2D(Node2D):
	def __init__(self, texture, position = [0, 0], rotation = 0, scale = [0, 0], parent = 'root'):
		super().__init__(parent, position = position, rotation = rotation, scale = scale, parent = parent)
		self.type_node = Nodes.Texture2D.value
		self.texture = Data(texture)

	def get_source(self):
		return {
					'id': self.id,
					'scale': self.scale,
					'parent': self.parent,
					'type': self.type_node,
					'rotation': self.rotation,
					'position': self.position,
					'texture': self.texture.data
		}