# list of bicycles
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

# first item in biclycles list
print(bicycles[0])

# formating element
print(bicycles[0].title())

# second item in biclycles list
print(bicycles[1])

# fourth item in the list
print(bicycles[3])

# last item in the list
print(bicycles[-1])

# using first item as a variable
message = "My first bicycle was a {}".format(bicycles[0].title())

print(message)
