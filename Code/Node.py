class Node:
    
	def __init__(self, _x, _y, _Can_Pass, _Weight, _Pre, _Is_chosed):
		self.x = _x
		self.y = _y
		self.Can_Pass = _Can_Pass
		self.Weight = _Weight
		self.Pre = _Pre
		self.Is_chosed = _Is_chosed
	
	def Pos(self):
		return [self.x, self.y]
	
	def Get_Can_Pass(self):
		return self.Can_Pass
		
	def Get_Is_chosed(self):
		return self.Is_chosed
	
	def Set_Is_chosed(self, _Is_chosed):
		self.Is_chosed = _Is_chosed
	
	def Get_Weight(self):
		return self.Weight
	
	def Set_Cost(self, _Cost):
		self.Cost = _Cost
	
	def Get_Cost(self):
		return self.Cost
	
	def Set_Weight(self, _Cost, _Node_Now, _End):
		self.Cost = _Cost + 1
		temp = self.Cost + abs(_End.Pos()[0] - self.x) + abs(_End.Pos()[1] - self.y)
		if temp < self.Weight and self.Is_chosed != 1 and self.Can_Pass != 1:
			self.Weight = self.Cost + abs(_End.Pos()[0] - self.x) + abs(_End.Pos()[1] - self.y)
			self.Pre = _Node_Now
			self.Is_chosed = 0
			
			if self.Pre.Pos()[0] == self.Pos()[0]:
				if self.Pre.Pos()[1] > self.Pos()[1]:
					self.Dir = '^'
				else:
					self.Dir = 'v'
			else:
				if self.Pre.Pos()[0] > self.Pos()[0]:
					self.Dir = '<'
				else:
					self.Dir = '>'
	
	def Get_Dir(self):
		return self.Dir
	
	def Get_Pre(self):
		return self.Pre
	