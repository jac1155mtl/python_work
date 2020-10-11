# My dinner guest list
guests = ['Dora','Snape','Lupin']

# Invite my guests

message = "Hello {}, would you like to go to dinner with me?".format(guests[0].title())

print(message)

message = "{}, {}, we're going out to dinner with {} tonight!".format(guests[1].title(), guests[2].title(), guests[0].title())

print(message)

# Dora can't make it
first_guest = guests.pop(0)

# Those who can make it
print(guests)

message = "Since {} had to go back to her dimension, it will be just you, {} and I for dinner this Friday".format(first_guest.title(),guests[0].title())

print(message)

message = "Since {} had to go back to her dimension, it will be just you, {} and I for dinner this Friday".format(first_guest.title(),guests[1].title())

print(message)

print(guests)
# New guests

#insert new guest at beginning of the lsit
guests.insert(0,'Alex')
print(guests)

# insert new guest in the middle of the list
guests.insert(2,'Sirius')
print(guests)

#insert new guest at the end of the list
guests.append('Paul')
print(guests)

# send new invitations
message = "Dear {}, since we just bought a bigger dinning table, you are invited to join us to dinner this coming Friday."

print(message.format(guests[0].title()))

print(message.format(guests[1].title()))

print(message.format(guests[2].title()))

print(message.format(guests[3].title()))

print(message.format(guests[4].title()))

#Shrinking guest list
new_message = "Dear {}, \nUnfortunately, our new table will not arrive in time and now can only two people for Friday's dinner party. \nI am sorry I can no longer invite you to dinner. \nSincerly,\nJo Ann."

first_rejected_guest = guests.pop(0)
second_rejected_guest = guests.pop(1)
third_rejected_guest = guests.pop(-1)

print(new_message.format(first_rejected_guest.title()))

print(new_message.format(second_rejected_guest.title()))

print(new_message.format(third_rejected_guest.title()))

# confirm invitations for remaining guests
last_message = "Hey {}, it will be the usual three of us for dinner this Friday."

print(last_message.format(guests[0].title()))

print(last_message.format(guests[1].title()))

# clean guests list
del guests[0]
del guests[0]
print(guests)
