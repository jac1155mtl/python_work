#list of my favourite foods
my_foods = ['pizza','falafel','carrot cake']

#copy my list of favourite foods for my friend
friend_foods = my_foods[:]

#add a new favourite food to my list
my_foods.append('cannoli')

#add a new favourite food to my friend's list
friend_foods.append('ice cream')

#print both lists - using for loop
print('My favourite foods are:')
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)
