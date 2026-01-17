num = float(input("Enter a number: "))

if num < 0:
    print("Cannot find the square root of a negative number.")
else:
    result = num ** 0.5
    print("The square root is:", result)