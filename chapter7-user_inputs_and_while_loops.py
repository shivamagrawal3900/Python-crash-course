# HOW THE INPUT() FUNCTION WORKS

# NOTE: Sublime Text and many other editors don’t run programs that prompt the user for input. 
# You can use these editors to write programs that prompt for input, 
# but you’ll need to run these programs from a terminal.

# The input() function takes one argument: the prompt, or instructions, 
# that we want to display to the user so they know what to do.
message = input("Enter message: ")
print(message)


# Using int() to Accept Numerical Input
# When you use the input() function, 
# Python interprets everything the user enters as a string.
age = input("Enter age: ")
print(type(age))
# ><class 'str'>

# The int() function converts a string representation of a number to a numerical representation
age = int(age)
print(type(age))
# ><class 'int'>

# NOTE: When you use numerical input to do calculations and comparisons, 
# be sure to convert the input value to a numerical representation first.


print() #line gap
# The Modulo Operator(%)
# divides one number by another number and returns the remainder
print(4%3)
# >1
print(5%3)
# >2
print(6%3)
# >0


print() #line gap
# INTRODUCING WHILE LOOPS
# The while Loop in Action
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
# >1
# >2
# >3
# >4
# >5

# Letting the User Choose When to Quit
prompt = "\ntell me something, and I'll repeat: "
prompt += "\nEnter 'quit' to exit: "
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
# Loop will continue until user enters 'quit'(case sensitive)

# Using break to Exit a Loop
prompt = "\nenter name of your city: "
prompt += "\nEnter 'quit' to exit: "
city = ""
while True:
	city = input(prompt)
	if city == 'quit':
		print('Exiting the loop now')
		break
	print(f"{city.title()} is a wondurful city")

print() #line gap
# Using continue in a Loop
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

# >unconfirmed_users: ['alice', 'brian', 'candice']
# >Verifing user: Candice
# >Verifing user: Brian
# >Verifing user: Alice

# >Following user are confirmed:
# >candice
# >brian
# >alice


# USING A WHILE LOOP WITH LISTS AND DICTIONARIES

# NOTE: A for loop is effective for looping through a list, 
# but you shouldn’t modify a list inside a for loop 
# because Python will have trouble keeping track of the items in the list. 
# To modify a list as you work through it, use a while loop.

print() #line gap
# Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

print(f"unconfirmed_users: {unconfirmed_users}")

# Below loop will continue untill the list is NOT EMPTY
while unconfirmed_users:
	# pop() removes from end, so confirmed_users list will be in reverse order
	current_user = unconfirmed_users.pop()
	print(f"Verifing user: {current_user.title()}")
	confirmed_users.append(current_user)

print("\nFollowing user are confirmed:")
for user in confirmed_users:
	print(user)

print() #line gap
# Removing All Instances of Specific Values from a List
# since remove() removes only single instance, 
# we can run loop while value is no longer present in list
pets = ['dog', 'cat', 'fish', 'cow', 'cat', 'sheep', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

# >['dog', 'cat', 'fish', 'cow', 'cat', 'sheep', 'cat']
# >['dog', 'fish', 'cow', 'sheep']


print() #line gap
# Filling a Dictionary with User Input
responses = {}

polling_active = True

while polling_active:
	name = input("\nEnter name: ")
	color = input("Favourate color: ")
	responses[name] = color

	repeat = input("Any more users(Enter yes/no): ")
	if repeat == 'no':
		polling_active = False

print("\n-----Poll results------")
for name, color in responses.items():
	print(f"{name.title()}'s favourate color is {color.lower()}")
