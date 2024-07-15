
class Rect:
	def __init__(self, position = [0,0], size = [0, 0], scale = [1, 1], rotation = 0):
		self.position = position
		self.rotation
		self.scale = scale
		self.size = size

	def get(self):
		return {	
					'rotation': rotation,
					'position': position,
					'scale': scale,
					'size': size
		}

	def update(self, dict1):
		dict1.update(self.get())
		return dict1
