
class Location:
	def __init__(self):
		self.objects = {}


	def add_node(self, node):
		self.objects[node.id] = node


	def delete_id_node(self, _id):
		self.objects.pop(_id)


	def delete_node(self, node):
		self.objects.pop(node.id)
