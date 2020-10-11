# a list of first 10 squares
squares1 = []
for value in range(1,11):
	square = value**2
	squares1.append(square)
print(squares1)

# a more concise version of creating the list
# without the temporary variable
squares2 = []
for value in range(1,11):
    squares2.append(value**2)
print(squares2)

# an even more consise version of creating the listing
# using list comprehension to create the listing
squares3 = [value**2 for value in range(1,11)]
print(squares3)
