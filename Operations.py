
class Operation():
	"""A class for modeling a basic operations calculator"""
	def __init__(self, operation, first_num, second_num):
		self.operation = operation
		self.first_num = first_num
		self.second_num = second_num

	def operation_result(self):
		if self.operation == "addition":
			return (self.first_num + self.second_num)
		if self.operation == "subtraction":
			return (self.first_num - self.second_num)
		if self.operation == "multiplication":
			return (self.first_num * self.second_num)
		if self.operation == "division":
			return (self.first_num / self.second_num)

