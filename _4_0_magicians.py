#print each magician's name
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

#print a message to each magician
magicians = ['alice','david','carolina']
for magician in magicians:
    print("{}, that was a great trick!".format(magician.title()))
    print("I can't wait to see your next trick, {}.\n".format(magician.title()))

#Thank the group of magicians
print("Thank you, everyone. That was a great magic show!")
