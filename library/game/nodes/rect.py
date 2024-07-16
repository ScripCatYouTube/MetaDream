
class Rect:
	def __init__(self, position = [0,0], size = [0, 0], scale = [1, 1], rotation = 0) -> None:
		self.position = position
		self.rotation
		self.scale = scale
		self.size = size
		self.defualt_size = size


	def get_two_corners_rect(self):
		return (
			(self.position[0], self.position[1]), # First left up corner
			(self.position[0] + self.size[0], self.position[1] + self.size[1]) # Second right down corner
		)


	def get(self) -> dict:
		return {	
					'rotation': rotation,
					'position': position,
					'scale': scale,
					'size': size
		}


	def update(self, dict1) -> dict:
		dict1.update(self.get())
		return dict1


	def change_size_by_scale(self, scale: list) -> None:
		self.size[0] = self.defualt_size[0] * scale[0]
		self.size[1] = self.defualt_size[1] * scale[1]


	def change_scale_by_size(self, size: list) -> None:
		try: 
			self.scale[0] = self.defualt_size[0] / size[0]
		except ZeroDivisionError: 
			self.scale[0] = 0

		try:
			self.scale[1] = self.defualt_size[1] / size[1]
		except ZeroDivisionError:
			self.scale[1] = 0


	def change_scale(self, scale: list) -> None:
		self.scale = scale


	def change_size(self, size: list) -> None:
		self.size = size


	def is_collision(self, rect: Rect) -> bool:
		self_corners = self.get_two_corners_rect()
		rect_corners = rect.get_two_corners_rect()


		if self_corners[0][0] <= rect_corners[1][0] and self_corners[1][0] >= rect_corners[0][0]: pass