import unittest
from Operations import Operation

class TestOperation(unittest.TestCase):
	"""Test for the Operation class"""
	def setUp(self):
		"""Create a set of numbers to test the operations"""
		self.positive_integer = 90
		self.negative_integer = -88
		self.positive_float = 45.96396

	def test_positive_integer_sum(self):
		"""Testing sum of positive integers"""
		new_operation = Operation("addition", self.positive_integer, self.positive_integer)
		self.assertEqual(new_operation.operation_result(), 180)

	def test_positive_negative_integer_sum(self):
		"""Testing sum of positive and negative integers"""
		new_operation = Operation("addition", self.positive_integer, self.negative_integer)
		self.assertEqual(new_operation.operation_result(), 2)

	def test_positive_integer_float_sum(self):
		"""Testing sum of positive integer and float"""
		new_operation = Operation("addition", self.positive_integer, self.positive_float)
		self.assertEqual(new_operation.operation_result(), 135.96396)

	def test_positive_integer_subtract(self):
		"""Testing subtract of positive integers"""
		new_operation = Operation("subtraction", self.positive_integer, self.positive_integer)
		self.assertEqual(new_operation.operation_result(), 0)

	def test_positive_negative_integer_subtract(self):
		"""Testing subtract of positive and negative integers"""
		new_operation = Operation("subtraction", self.positive_integer, self.negative_integer)
		self.assertEqual(new_operation.operation_result(), 178)

	def test_positive_integer_float_subtract(self):
		"""Testing subtract of positive integer and float"""
		new_operation = Operation("subtraction", self.positive_integer, self.positive_float)
		self.assertEqual(new_operation.operation_result(), 44.03604)

	def test_positive_integer_multiply(self):
		"""Testing multiplication of positive integers"""
		new_operation = Operation("multiplication", self.positive_integer, self.positive_integer)
		self.assertEqual(new_operation.operation_result(), 8100)

	def test_positive_negative_integer_multiply(self):
		"""Testing multiplication of positive and negative integers"""
		new_operation = Operation("multiplication", self.positive_integer, self.negative_integer)
		self.assertEqual(new_operation.operation_result(), -7920)

	def test_positive_integer_float_multiply(self):
		"""Testing multiplication of positive integer and float"""
		new_operation = Operation("multiplication", self.positive_integer, self.positive_float)
		self.assertEqual(new_operation.operation_result(), 4136.7564)

	def test_positive_integer_divide(self):
		"""Testing division of positive integers"""
		new_operation = Operation("division", self.positive_integer, self.positive_integer)
		self.assertEqual(new_operation.operation_result(), 1)

	def test_positive_negative_integer_divide(self):
		"""Testing division of positive and negative integers"""
		new_operation = Operation("division", self.positive_integer, self.negative_integer)
		self.assertEqual(new_operation.operation_result(), -1.0227272727272727)

	def test_positive_integer_float_divide(self):
		"""Testing division of positive integer and float"""
		new_operation = Operation("division", self.positive_integer, self.positive_float)
		self.assertEqual(new_operation.operation_result(), 1.9580558333094016)


if __name__ == '__main__':
	unittest.main()
