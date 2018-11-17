class Statistic:
	def __init__(self):
		self.kills = 0
		self.score = 0
		self.time = 0

	def getKills(self):
		return self.kills

	def getScore(self):
		return 0

	def plusKill(self, confirm):
		if confirm:
			self.kills += 1

	def setTime(self, time):
		self.time = time

	#list(minutes, seconds)
	def getTime(self):
		return (self.time * 1000 * 60 % 60, self.time * 1000 % 60)
