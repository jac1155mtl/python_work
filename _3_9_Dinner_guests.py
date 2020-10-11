# My dinner guest list
guests = ['Dora','Snape','Lupin']

# Invite my guests
message = "\nHello {}, would you like to go to dinner with me?".format(guests[0].title())
print(message)

message = "\n{}, {}, we're going out to dinner with {} tonight!".format(guests[1].title(), guests[2].title(), guests[0].title())
print(message)

#message with the number of guests
message = '\nHey mom. I am having dinner with {} guests tonight. Your introvert daughter is socializing!'.format(len(guests))
print(message)
