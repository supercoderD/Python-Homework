
user_input = input("Enter some text: ")
has_number = any(char.isdigit() for char in user_input)


if has_number:
    print("Yes, there is at least one number in your input.")
else:
    print("No numbers were found.")
