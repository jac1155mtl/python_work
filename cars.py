cars = ['bmw', 'audi', 'toyota', 'subaru']

#sort in alphabetical order
cars.sort()
print(cars)

#sort in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

#temporarily sort the list
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
