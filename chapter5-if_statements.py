cars = ['Audi', 'BMW', 'Jaguar', 'LandRover']

for car in cars:
	if car == 'Jaguar':
		print(car.upper())
	else:
		print(car)

# == is case sensitive
print(cars[1]=='bmw') 
# > False

# !=
print(cars[1]!='Audi')
# > True

# Numerical Comparisions

# ==, !=, <, >, <=, >=

# Checking multiple values

# 'and' and 'or' operations. NOTE: '&' and '|' does not work
print(cars[0]=='Audi' and cars[1] == 'BMW')
# >True
print(cars[2]=='Jaguar' or cars[3]=='Jaguar')
# >True

# First 'and' operations takes place then or
print(cars[2]=='Jaguar' and cars[3]=='Jaguar' or  cars[0]=='Audi' and cars[1] == 'Audi')
# >False

# To check if the value is in list, use 'in' keyword
print('Jaguar' in cars)
# >True

# To check if the value is not in the list, use 'not in' keyword
print('Tata' not in cars)
# >True

# IF STATEMENTS

# NOTE: assignment in if won't work, i.e. if a=2 will give an error
# If - elif - else statements
value=15
if value%15 == 0:
	print('buzzfizz')
elif value%3 == 0:
	print('buzz')
elif value%5 == 0:
	print('fizz')
else:
	print('none')


# To check if list is empty

toppings = []

if toppings:
	print('toppings are: '+str(toppings))
else:
	print('no toppings')
# >no toppings

# For pEP 8 styling, use singe space both sides of operator