magicians = ['alice', 'david', 'carlos']

# looping through a list, using 'for' loop
for magician in magicians:
	print(magician)


# processing with a loop and after the loop
for magician in magicians:
	print(f"{magician.title()}, that was a great trick")
	print(f"I can't wait to see your next trick, {magician.title()}\n")

print("Thank you everyone, that was a great show")


# Python uses indentation to determine how a line or group of lines are realted to eachother
# Code relies on proper indentation, or there will be errors

# Missing to indent first line will lead to indentation error
# This will lead to IndentationError: expected an indented block
# for magician in magicians:
# print(f"{magician.title()}, that was a great trick") 

# Missing to indent in additional lines won't produce error 
# but will lead to unexpected behaviour
# Output won't be same as last time
for magician in magicians:
	print(f"{magician.title()}, that was a great trick")
print(f"I can't wait to see your next trick, {magician.title()}")
# once the loop finishes execution, the "magician" will hold the last value of the list

# Unnecessary indentions are also not allowed
# This will lead to IndentationError: unexpected indent
# message = "Hello world!!"
# 	print(message)

# Just noticied, indentation could be of any number of spaces and tabs
# but it should be same for a block
# and different blocks can have different indentations
# i.e. two for loops can have different indentations in same program


# Indentating unnecessarly after the loop will also lead to logical error, but the program will run
# This will print last statement for each element in loop, instead of printing just once
for magician in magicians:
	print(f"{magician.title()}, that was a great trick")
	print(f"I can't wait to see your next trick, {magician.title()}\n")

	print("Thank you everyone that was a great show.")



# Forgetting the colen after for will lead to syntax error
# for magician in magicians
# 	print(f"{magician.title()}, that was a great trick")


## NUMERICAL LISTS

# Using range() to create lists

# range() is used to generate series of numbers
# range(starting_number_inclusive, ending_number_exclusive)
for value in range(1, 5):
	print(value)


# range(end_number_exclusive_starting_from_0)
for value in range(5):
	print(value)


# to convert range to list, pass range to list() method as argument
print(list(range(1,5)))


# range() can take step size as 3rd param
# step size need to be an integer
for value in range(1, 11, 2):
	print(value)


# To get a list of squares 1 to 10
square_numbers = []
for value in range(1, 11):
	square_numbers.append(value**2)
print(square_numbers)


# range() only prints in ascending order
# so below code does not print anything 
for value in range(-1, -10):
	print(value)


# Simple stats with list of numbers

# getting min, max and sum
l = [1,2,3,4,5,6,7]
print('min is: '+str(min(l)))
print('max is: '+str(max(l)))
print('sum is: '+str(sum(l)))


# list comprehensions

square_numbers = [value**2 for value in range(1, 11)]
print(square_numbers)


# WORKING WITH PART OF A LIST

# getting a sublist of a list is called slicing the list
# as we are getting a slice of the list
# list[initial_index_inclusive : last_index_exclusive]
print(square_numbers[0:3])

# index out of bound does not occur with slicing
# it just returs an empty list
print(square_numbers[1:1])

# any index can be omitted from slice
# all till index 3
print(square_numbers[:3])
# all after 3
print(square_numbers[3:])
# also works with -ve indexes
print(square_numbers[-3:])

# 3rd param with elements to skip(kinda like step size) can also be added
print(square_numbers[1:-1:2])


# COPYING A LIST
# just don't pass any index while slicing
# this will create a NEW LIST
square_numbers_2 = square_numbers[:]
square_numbers_2.pop(0)
print(str(square_numbers_2) +'\n'+ str(square_numbers))



## TUPLES
# An immutable list is called a tuple

rectangle = (50, 200)
print(rectangle[0])
print(rectangle)

# Below code will raise an error as tuples are immutable
# error: 'tuple' object does not support item assignment
# rectangle[0] = 100

# while initiating a tuple with single element, it needs to include a trailing comma
# else it will be considered a primitive type
my_tp = (1,)
print(my_tp[0])
# an additional trailing comma can be added to tuple with more than one values as well. No issues in that

# Looping through a tuple
# same as in a list
for value in rectangle:
	print(value)

# Although you can't modify the tuple but you can assign a new value to the variable holding that tuple
dimensions = (10, 200)
print('initial dimensions: '+str(dimensions))
dimensions = (150, 100)
print('updated dimensions: '+str(dimensions))

# other methods like max, min and sum will also work on tuple
print(sum(dimensions))
# however sorted() will work by sort() won't as tuples are immutable
print(sorted(dimensions))


## STYLING YOUR CODE
# follow PEP 8
# PEP stands for Python Enhancement Proposal