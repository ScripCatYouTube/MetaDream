from .nodes.node import Node
from .nodes.utils.rect import Rect

class Location:
	def __init__(self) -> None:
		self.objects = {}


	def add_node(self, node) -> None:
		self.objects[node.id] = node


	def delete_id_node(self, _id) -> None:
		self.objects.pop(_id)


	def delete_node(self, node) -> None:
		match self.choose_parent_type(node, Node, str):
			case 0:
				self.objects.pop(node.id)

			case 1:
				self.objects.pop(node)


	def update_value(self, _node, key, value) -> None:
		node = None

		match self.choose_parent_type(_node, str, Node):
			case 0:
				node = self.objects[_node]

			case 1:
				node = _node

		setattr(node, key, value)


	def get_value(self, _node, key) -> object:
		node = None

		match self.choose_parent_type(_node, str, Node):
			case 0:
				node = self.objects[_node]

			case 1:
				node = _node		

		return getattr(node, key)


	def choose_parent_type(self, value, *types, text_type_error = 'The attribute \'node\' is not Node or string ID') -> int:
		for n, i in enumerate(types):
			if i == type(value).__mro__[-2]:
				return n

		raise TypeError(text_type_error)


	def camera_rect(self, rect: Rect) -> list:
		objects = []

		for i in self.objects:
			node = self.objects[i].rect

			if rect.is_collision(node):
				objects += node.get_source()

		return objects


	def camera_node(self, node: Node) -> list:
		return self.camera_rect(
			node.rect
		)
