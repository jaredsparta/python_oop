# getters and setters


# class Student:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
# 
#     # __ are used to hide variables
#     # The @ is a decorator that is any callable python object used to modify
#     # a function or class
#     @property
#     def Student(self, value):
#         return self.__name
# 
#     
#     @Student.setter
#     def Student(self, value):
#         self.__name = value
#     
# jared = Student("Jared", "SG")
# 
# print(jared.name)

class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# using property decorator 
	# a getter function 
	#@property
	#def age(self): 
	#	print("getter method called") 
	#	return self._age 
	
	# a setter function 
	@age.setter 
	def age(self, a): 
		if(a < 18): 
			raise ValueError("Sorry you age is below eligibility criteria") 
		print("setter method called") 
		self._age = a 

mark = Geeks() 
print(mark.age)
mark.age = 19
print(mark.age)
mark.age = 51
print(mark.age)
