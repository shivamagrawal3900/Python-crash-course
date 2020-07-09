# Chapter 3: Introducing Lists

# To create list:
bicycles = ['hero', 'mountain', 'street']

# To print list:
print(bicycles)

# Access element via index
print(bicycles[0])

# Index works in -ve as well
print(bicycles[-1])

# "IndexError: list index out of range" error could occur if index is out of range
# valid for both +ve and -ve indexes
# print(bicycles[-100])

# Modify a list element
bicycles[0] = 'trek'
print(bicycles)

# Append an element
bicycles.append('honda')
print(bicycles)

# Inserting an element
bicycles.insert(2, 'suzuki')
print(bicycles)

# Removing elements via index
del bicycles[-1]
print(bicycles)
# "del" does not return the element
# below would be an invalid syntax
# print(del bicycles[-1])

# To get and remove the element via index
# pop() with no arguments would remove the last element
print(bicycles.pop())
print(bicycles)
# pop(index) to remove and get argument from specified index
print(bicycles.pop(0))
print(bicycles)


# To remove an element by value
# "remove" does not return the element
# it only removes the first occurance of the element
bicycles.remove('mountain')
print(bicycles)


cars = ['maruti', 'hundai', 'honda', 'ford', 'renault']
print(cars)
# Sorting a list
# via sort() method. It'll sort the list and won't return anything
cars.sort()
print(cars)
# To reverse sort
cars.sort(reverse=True)
print(cars)

# To return a sorted list
# by "sorted" actual list will remain the same
print(sorted(cars))
print(cars)

# To reverse the list
# It will reverse the actual list
cars.reverse()
print(cars)

# To find length of the list
print(len(cars))


