# My dinner guest list
guests = ['Dora','Snape','Lupin']

# Invite my guests

message = "Hello {}, would you like to go to dinner with me?".format(guests[0].title())

print(message)

message = "{}, {}, we're going out to dinner with {} tonight!".format(guests[1].title(), guests[2].title(), guests[0].title())

print(message)
