#Objective: use every function for accessing and modifying a list

#list of languages
languages = ['French','English','Creole','German','Italian','Japanese']

print(languages)

#ACCESSING ELEMENTS OF A LIST

##my mothertongue
print(
    '\nMy mother tongue is {}.'.format(languages[0])
)

##
print(
    '\nI have never learned {} or {}.'.format(languages[-2],languages[-1])
)

# MODIFYING ELEMENTS OF THE LIST

## change Italian to Spanish
languages[4]='Spanish'
print('\nChanged Italian to Spanish')
print(languages)

# ADDING ELEMENTS TO A LIST

## re-add Italian to the list, using append() method
languages.append('Italian')
print('\nRe-adding Italian to the list:')
print(languages)

## add Latin, using insert() method
languages.insert(4-1,'Latin')
print('Added Latin in 4-th position')
# REMOVING ELEMENTS

## remove Italian, using del statement
del languages[-1]
print('\nDeleted Italian')
print(languages)

## remove Latin using pop method [by position]
dead_language = languages.pop(4-1)
print(
    "\n{} is a dead language that doesn't impact my day-to-day.".format(dead_language)
)
print(languages)

## remove Japanese using remove() method [by value]
new_language = 'Japanese'
languages.remove(new_language)
print(
    '\nDeleted {} since I have not started learning it yet'.format(new_language)
)
print(languages)

# ORGANIZING A LIST

## print original list
print('Here is the original list:')
print(languages)

## print the list sorted alphabetically without modifying it
print('\nHere is the list, temporarily sorted in alphabetical order:')
print(sorted(languages))

## print original list again
print('\nHere is the sorted list again:')
print(languages)

## print the list in reverse alphabetical order, without modifying it
print('\nHere is the list, temporarily sorted in reverse alphabetical order:')
print(sorted(languages,reverse=True))

## print the original list again
print('\nHere is the list in its original order:\n')
print(languages)

## print the list in reverse order
languages.reverse()
print('\nHere is the list in reverse order:')
print(languages)

## revert list to original order
languages.reverse()
print('\nHere is the list back in its original order')
print(languages)

## permanently change list to reverse alphabetical order
languages.sort(reverse=True)
print('\nThe list is now permanently stored in reverse alphabetical order:')
print(languages)
