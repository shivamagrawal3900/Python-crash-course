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

