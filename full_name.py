#Ada Lovelace name in parts
first_name = "ada"
last_name = "lovelace"

# if in Python 3.6 or higher
#full_name = f"{first_name} {last_name}"
#print(f"Hello, {full_name.title()}!")
#message = f"Hello, {full_name.title()}!"
#print(message)

# if in Python 3.5 or earler

# combine name and print
full_name = "{} {}".format(first_name, last_name)
print(full_name)

#greeting Ada Lovelace and title casing her name
print("{} {}{}".format("Hello,", full_name.title(),"!"))

# storing greeting in variable MESSAGE and printing it
message = "{} {}{}".format("Hello,", full_name.title(),"!")
print(message)

#adding whitespaces
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
