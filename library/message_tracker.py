from datetime import datetime

class MessageTracker:
	def __init__(self, time = [0,0,0,10]) -> None: # (10 seconds) time in list until the message is deleted
		self.time = time

		# the list of temporary message. 
		# Element example: {
		#	'time': [18, 12, 45, 10],
		#	'data': {'code': 0} 
		#   }
		#
		# time format: [day, hours, minuts, seconds] 
		self.messages = []

	def page_get_messages(self) -> dict:
		self.clear_timeout_messages()
		return self.get_messages()

	def add_message(self, message) -> None:
		self.messages.append({'time': self.get_now_time(), 'data': message})


	def isnt_timeout_message(self, message) -> bool:
		if self.get_now_time() > self.add_lists(self.time, message['time']):
			return True
		return False

	def clear_timeout_messages(self) -> None:
		new_messsages = {}
		for i in self.messages:
			if isnt_timeout_message(i):
				new_messsages[i['time']] = i['data']

		self.messages = new_messsages

	def get_now_time(self) -> list:
		time = datetime.now()
		return [time.day, time.hour, time.minute, time.second]

	def add_lists(self, list_a, list_b) -> list:
		for index, num in enumerate(list_a):
			try: 
				list_b[index] += num
			except IndexError: 
				list_b.append(num)
			except TypeError:
				list_b[index] = num
		return list_b

	@staticmethod
	def transform_time(t) -> list:
		return [
		t // 86400, # days
		t // 3600 % 24, # hours
		t // 60 % 60, # minutes
		t % 60 # seconds
		]