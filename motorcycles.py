#list of motorcycle manufactors
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# change honda to ducatti
motorcycles[0] = 'ducati'
print(motorcycles)

# add honda to end of the list
motorcycles.append('honda')
print(motorcycles)

# insert Harley-Davidson at the beginning of the list
motorcycles.insert(0,'harley-davidson')
print(motorcycles)

# remove first item in the list
del motorcycles[0]
print(motorcycles)

# remove last item of the motorcycles list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print('The last motorcycle I owned was a {}'.format(popped_motorcycle.title()))

#pop first item in list
first_motorcycle = motorcycles.pop(0)
print('The first motorcycle I owned was a {}'.format(first_motorcycle.title()))

#remove item by value
motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('{} is too expensive for me.'.format(too_expensive.title()))
