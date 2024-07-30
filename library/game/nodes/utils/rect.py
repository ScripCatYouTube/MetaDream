
class Rect:
	def __init__(self, position = [0,0], size = [0, 0], scale = [1, 1], rotation = 0) -> None:
		self.position = position
		self.rotation = rotation
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
					'rotation': self.rotation,
					'position': self.position,
					'scale': self.scale,
					'size': self.size
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


	def is_collision(self, rect) -> bool:
		self_corners = self.get_two_corners_rect()
		rect_corners = rect.get_two_corners_rect()

		return self.collided(self_corners, rect_corners)


	def collided(self, r1, r2) -> bool:
		if r1[1][0] >= r2[0][0] and r1[0][0] <= r2[1][0] and r1[1][1] >= r2[0][1] and r1[0][1] <= r2[1][1]:
			return True

		return False
