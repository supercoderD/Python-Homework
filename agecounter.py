try:
    age=26
    age2=int(input("Enter the age."))
    if age==age2:
        print("Congrats, you won the game.")
    if age2%2==0:
        print("The age is even.")
    if age2%2!=0:
        print("The age is odd.")
except ValueError:
    print("Invalid.")



