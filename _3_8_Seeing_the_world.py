# list of five places in the world you'd like to visit
places = ['Tokyo','Bretagne','New York','Melbourne','San Francisco']

# print original list
print('Here is the original list:')
print(places)

# print the list sorted alphabetically without modifying it
print('\nHere is the list, temporarily sorted in alphabetical order:')
print(sorted(places))

# print original list again
print('\nHere is the sorted list again:')
print(places)

# print the list in reverse alphabetical order, without modifying it
print('\nHere is the list, temporarily sorted in reverse alphabetical order:')
print(sorted(places,reverse=True))

# print the original list again
print('\nHere is the list in its original order:\n')
print(places)

#print the list in reverse order
places.reverse()
print('\nHere is the list in reverse order:')
print(places)

#revert list to original order
places.reverse()
print('\nHere is the list back in its original order')
print(places)

#permanently change list to reverse alphabetical order
places.sort(reverse=True)
print('\nThe list is now permanently stored in reverse alphabetical order:')
print(places)
