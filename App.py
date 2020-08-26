from tkinter import *
from Operations import Operation

class Application():
	"""A class for modeling a simple calculator GUI with tkinter"""
	def __init__(self, master=None):
		"""Class attributes"""
		self.f_num = 0
		self.math = ""

		"""Creating screen elements"""
		self.e = Entry(master, width=23, borderwidth=5, font=("Helvetica", 25))

		self.button_1 = Button(master, text="1", padx=50, pady=20, command=lambda: self.button_click(1))
		self.button_2 = Button(master, text="2", padx=50, pady=20, command=lambda: self.button_click(2))
		self.button_3 = Button(master, text="3", padx=50, pady=20, command=lambda: self.button_click(3))
		self.button_4 = Button(master, text="4", padx=50, pady=20, command=lambda: self.button_click(4))
		self.button_5 = Button(master, text="5", padx=50, pady=20, command=lambda: self.button_click(5))
		self.button_6 = Button(master, text="6", padx=50, pady=20, command=lambda: self.button_click(6))
		self.button_7 = Button(master, text="7", padx=50, pady=20, command=lambda: self.button_click(7))
		self.button_8 = Button(master, text="8", padx=50, pady=20, command=lambda: self.button_click(8))
		self.button_9 = Button(master, text="9", padx=50, pady=20, command=lambda: self.button_click(9))
		self.button_0 = Button(master, text="0", padx=50, pady=20, command=lambda: self.button_click(0))

		self.button_add = Button(master, text="+", padx=50, pady=20, command=self.button_add)
		self.button_equal = Button(master, text="=", padx=109, pady=20, command=self.button_equal)
		self.button_clear = Button(master, text="Clear", padx=97, pady=20, command=self.button_clear)
		self.button_subtract = Button(master, text="-", padx=51, pady=20, command=self.button_subtract)
		self.button_multiply = Button(master, text="*", padx=53, pady=20, command=self.button_multiply)
		self.button_divide = Button(master, text="/", padx=51, pady=20, command=self.button_divide)

		"""Placing screen elements"""
		self.e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

		self.button_1.grid(row=3, column=0)
		self.button_2.grid(row=3, column=1)
		self.button_3.grid(row=3, column=2)

		self.button_4.grid(row=2, column=0)
		self.button_5.grid(row=2, column=1)
		self.button_6.grid(row=2, column=2)

		self.button_7.grid(row=1, column=0)
		self.button_8.grid(row=1, column=1)
		self.button_9.grid(row=1, column=2)

		self.button_0.grid(row=4, column=0)
		self.button_add.grid(row=5, column=0)
		self.button_equal.grid(row=5, column=1, columnspan=2)
		self.button_clear.grid(row=4, column=1, columnspan=2)

		self.button_subtract.grid(row=6, column=0)
		self.button_multiply.grid(row=6, column=1)
		self.button_divide.grid(row=6, column=2)

	def button_click(self, number):
		current = self.e.get()
		self.e.delete(0, END)
		self.e.insert(0, str(current) + str(number))

	def button_clear(self):
		self.e.delete(0, END)

	def set_operation(self, math):
		first_number = self.e.get()
		self.math = math
		self.f_num = int(first_number)
		self.e.delete(0, END)

	def button_add(self):
		self.set_operation("addition")

	def button_subtract(self):
		self.set_operation("subtraction")

	def button_multiply(self):
		self.set_operation("multiplication")

	def button_divide(self):
		self.set_operation("division")

	def button_equal(self):
		second_number = int(self.e.get())
		self.e.delete(0, END)

		new_result = Operation(self.math, self.f_num, second_number)
		self.e.insert(0, new_result.operation_result())


root = Tk()
root.title("PyCalculator")
Application(root)
root.mainloop()