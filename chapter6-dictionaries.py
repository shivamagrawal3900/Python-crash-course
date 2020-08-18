alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# >green
# >5

# A dictionary in Python is a collection of key-value pairs. 
# Each key is connected to a value, and you can use a key to access the value associated with that key. 
# A key’s value can be a number, a string, a list, or even another dictionary. 


# you can add new key-value pairs to a dictionary at any time
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# >{'color': 'green', 'points': 5}
# >{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# NOTE: As of Python 3.7, dictionaries retain the order in which they were defined. 
# 	When you print a dictionary or loop through its elements, you will see the elements 
# 	in the same order in which they were added to the dictionary.

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'red'
print(alien_0)
# >{'color': 'red'}

# Modifying Values in a Dictionary
alien_0['color'] = 'yellow'
print(alien_0)
# >{'color': 'yellow'}


# Removing Key-Value Pairs
alien_0 = {'color' : 'red', 'points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# >{'color': 'red', 'points': 5}
# >{'color': 'red'}


# A Dictionary of Similar Objects
# You can also use a dictionary to store one kind of information about many objects. 
favourite_language = {
	'jen': 'java',
	'saraha': 'scala',
	'phil': 'swift',
	}

# NOTE: It’s good practice to include a comma after the last key-value pair as well, 
# 	so you’re ready to add a new key-value pair on the next line.


# Using get() to Access Values
# Using keys in square brackets to retrieve the value you’re interested in from a dictionary 
# might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.
alien_0 = {'color': 'green', 'speed': 'fast'}
# print(alien_0['points'])
# >KeyError: 'points'

# For dictionaries, specifically, you can use the get() method to set a default value 
# that will be returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. 
# As a second optional argument, you can pass the value to be returned if the key doesn’t exist
print(alien_0.get('points', 'No points value assigned'))
# >No points value assigned
# If optional default value is not provided, None will be returned but not Error

## LOOPING THROUGH A DICTIONARY


user_0 = {
	'username': 'sAgrawal',
	'first': 'Shivam',
	'last': 'Agrawal',
}

# the method items() returns a list of key-value pairs.
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

# >Key: username
# >Value: sAgrawal

# >Key: first
# >Value: Shivam

# >Key: last
# >Value: Agrawal

print() #line gap
# Looping Through All the Keys in a Dictionary
# use method keys() to return list of keys
for key in user_0.keys():
	print(f"key: {key}")

# >key: username
# >key: first
# >key: last

print() #line gap
# Looping through the keys is actually the default behavior when looping through a dictionary, 
# so this code would have exactly the same output
for key in user_0:
	print(f"key: {key}")

# >key: username
# >key: first
# >key: last

print() #line gap
# You can also use the keys() method to find out if a particular key is present
if 'middle' not in user_0.keys():
	print(f"middle name not present for user: {user_0['username']}\n")

# >middle name not present for user: sAgrawal


# Looping Through a Dictionary’s Keys in a Particular Order
# Starting in Python 3.7, looping through a dictionary returns the items in the same order they were inserted. 
# Sometimes, though, you’ll want to loop through a dictionary in a different order.
favourite_language = {
	'jen': 'java',
	'saraha': 'scala',
	'phil': 'swift',
	}

for name in sorted(favourite_language.keys()):
	print(f"Thank you {name.title()} for taking the poll")

# >Thank you Jen for taking the poll
# >Thank you Phil for taking the poll
# >Thank you Saraha for taking the poll

print() #line gap
# Looping Through All Values in a Dictionary
# use the values() method to return a list of values without any keys
for language in favourite_language.values():
	print(language.title())

# >Java
# >Scala
# >Swift

print() #line gap
# This approach pulls all the values from the dictionary without checking for repeats.
# To see each without repetition, we can use a set()
for language in set(favourite_language.values()):
	print(language.title())

# >Swift
# >Java
# >Scala

print() #line gap
# NOTE: You can build a set directly using braces and separating the elements with commas:
languages = {'Java', 'Scala', 'Swift', 'Java'}
print(languages)

# >{'Java', 'Swift', 'Scala'}
# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. 
# When you see braces but no key-value pairs, you’re probably looking at a set. 
# Unlike lists and dictionaries, sets do not retain items in any specific order.

print() # line gap
# NESTING

# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 10}
alien_1 = {'color': 'yellow', 'points': 15}
alien_2 = {'color': 'red', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# >{'color': 'green', 'points': 10}
# >{'color': 'yellow', 'points': 15}
# >{'color': 'red', 'points': 20}

print() #line gap
# A more realistic example would involve more than three aliens 
# with code that automatically generates each alien.

# Empty list
aliens = []

# Make 30 aliens
for i in range(0, 30):
	slow_alien = {'color': 'green', 'points': 10, 'speed': 'slow'}
	aliens.append(slow_alien)

# Show first 5 aliens
for alien in aliens[:5]:
	print(f"Alien: {alien}")

# Show total number of aliens
print(f"Total number of aliens: {len(aliens)}")

# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Total number of aliens: 30

print() #line gap
# to change the first three aliens to yellow, medium-speed aliens worth 10 points each
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 15
		alien['speed'] = 'medium'

# Show first 5 aliens
for alien in aliens[:5]:
	print(f"Alien: {alien}")

# Show total number of aliens
print(f"Total number of aliens: {len(aliens)}")

# >Alien: {'color': 'yellow', 'points': 15, 'speed': 'medium'}
# >Alien: {'color': 'yellow', 'points': 15, 'speed': 'medium'}
# >Alien: {'color': 'yellow', 'points': 15, 'speed': 'medium'}
# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Alien: {'color': 'green', 'points': 10, 'speed': 'slow'}
# >Total number of aliens: 30

print() #line gap
# A List in a Dictionary

pizza = {
	"crust": "Thick",
	"toppings": ["Mushroom", "Olive"],
}

print(f"The pizza has {pizza['crust']} crust, with toppings:")
for topping in pizza["toppings"]:
	print(f"\t{topping}")

# >The pizza has Thick crust, with toppings:
# >	Mushroom
# >	Olive

print() #line gap
# To traverse through each object's list
favourite_language = {
	"sarah": ["C++", "java"],
	"edward": ["Scala"],
	"jen": ["Go", "Java"]
}

for name, languages in favourite_language.items():
	print(f"{name} likes:")
	for language in languages:
		print(f"\t{language}")

# >sarah likes:
# >	C++
# >	java
# >edward likes:
# >	Scala
# >jen likes:
# >	Go
# >	Java

print() #line gap
# A dictionay in dictionary

users = {
	"aeinstein": {
		"first": "albert",
		"last": "einstein",
		"location": "princeton",
	},
	"mcurie": {
		"first": "marie",
		"last": "curie",
		"location": "paris",
	},
}

for username, user_info in users.items():
	print(f"\nusername: {username}")
	name = user_info['first'].title() +" "+user_info['last'].title()
	print(f"fullname: {name}")
	print(f"location: {user_info['location']}")


# >username: aeinstein
# >fullname: Albert Einstein
# >location: princeton

# >username: mcurie
# >fullname: Marie Curie
# >location: paris

# Notice that the structure of each user’s dictionary is identical. 
# Although not required by Python, this structure makes nested dictionaries easier to work with. 
# If each user’s dictionary had different keys, the code inside the for loop would be more complicated.