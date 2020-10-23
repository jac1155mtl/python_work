#from 4.9 - cube comprehensions
#use list comprehension to create list of first 10 cubes
cubes = [value**3 for value in range(1,11)]
print(cubes)

# print the first three items in the list
print('The first three items in the list are:')
print(cubes[:3])

#print three items from the middle of the list
print('\nThree items from the middle of the list are:')
print(cubes[4:7])

#print the last three items of the list
print('\nThe last three items in the list are:')
print(cubes[-3:])
