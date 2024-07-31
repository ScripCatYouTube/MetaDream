from .node2d import Node2D
from .nodes import Nodes
from library.game.nodes.utils.data import Data


class Camera2D(Node2D):
	def __init__(self, texture, zoom = [1,1], is_enabled = False, smooth_position = None, smooth_rotation = None, position = [0, 0], rotation = 0, scale = [0, 0], parent = 'root'):
		super().__init__(parent, position = position, rotation = rotation, scale = scale, parent = parent)
		self.type_node = Nodes.Texture2D.value
		self.smooth_position = smooth_position
		self.smooth_rotation = smooth_rotation
		self.is_enabled = is_enabled
		self.texture = Data(texture)
		self.zoom = zoom


	def get_node(self):
		return {
					'id': self.id,
					'zoom': self.zoom,
					'type': self.type_node,
					'parent': self.parent,
					'is_enabled': self.is_enabled,

					# if none, position smoothing is disabled. if any number position smoothing is enabled
					'smooth_position': self.smooth_position,
					# Same as for smooth_position
					'smooth_rotation': self.smooth_rotation
					
		}

