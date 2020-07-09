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


# NUMERICAL LISTS

