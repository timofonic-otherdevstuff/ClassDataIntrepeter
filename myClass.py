class DartmouthClass:
	number = '0'
	year = '0'
	term = '0'
	dids = []
	date = 0
	def __init__(self):
		self.dids = []
		self.number = '0'
		self.year = '0'
		self.term = '0'
		print("created class")

	def setNumber(self, number):
		self.number = number

	def getNumber(self):
		return self.number

	def setYear(self, year):
		self.year = year

	def getYear(self):
		return self.year

	def setTerm(self, term):
		self.term = term
	def getTerm(self):
		return self.term

	def appendDid(self, id):
		self.dids.append(id)
		#print(id)
	def getDid(self):
		return self.dids

	def setDate(self):
		temp = .1
		if (self.term == "Winter"):
			temp = .1
		elif (self.term == "Spring"):
			temp = .2
		elif (self.term == "Summer"):
			temp = .3
		else:
			temp = .4

		#print self.term
		self.date = int(self.year) + temp
		#print self.date
	def getDate(self):
		return self.date


