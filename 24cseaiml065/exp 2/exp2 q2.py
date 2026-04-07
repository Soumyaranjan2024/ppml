first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name (optional, press Enter if none): ")
last_name = input("Enter your last name: ")
if middle_name:
    full_name = first_name + " " + middle_name + " " + last_name
else:
    full_name = first_name + " " + last_name

print("Your full name is:", full_name)