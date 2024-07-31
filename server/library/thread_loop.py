from threading import Thread 

class ThreadLoop:
	def __init__(self, server):
		self.server = server

		self.start_thread()


	def start_thread(self):
		self.thread = Thread(target=self.run_thread, daemon=False)
		self.thread.start()


	def run_thread(self):
		while True:
			for i in self.server.players.users:
				self.server.players.users[i].loop()
