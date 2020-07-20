# message = "hello python world!!!"
# print(message)

# "This is a string"
# 'This is also a string'

# '"Double quotes in single quotes"'
# "'Single quotes in Double quotes'"


# f_name = "   shivam"
# l_name = "agrawal   "

# full_name = f'{f_name} {l_name}'

# print(f"Hi {full_name.title().strip()}!!")


# def say_hello(one, two = "hh"):
# 	print("Hello " + one + two)


# say_hello("abc", two = "bad")


class Student:

	school = "SVM"

	def __init__(self):
		self.a = '10'


	def call_me(self, a, **kwargs):
		print(kwargs)

	@classmethod
	def print_it(cls):
		print("This is print statement " + cls.school)

	@staticmethod
	def print_static(sld):
		print("This is static method " + sld.a)


s1 = Student()

s1.call_me("haha")

Student.print_it()

s1.print_static(s1)

# s1.print_static(s1)

a = [2]
if len(a) == 1:
	print(a.pop())
else:
	print("two")

print(len(a))