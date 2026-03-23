num=int(input("Enter a number: "))
if num<0 and num>=10:
    print("This number is 1 digit long")
elif num>=10 and num<100:
    print("This number is 2 digits long")
elif num>=100 and num<1000:
    print("This number is 3 digits long")
elif num>=1000 and num<10000:
    print("This number is 4 digits long")
elif num>=10000 and num<100000:
    print("This number is 5 digits long")
elif num>=100000 and num<1000000:
    print("This number is 6 digits long")
elif num>=1000000 and num<10000000:
    print("This number is 7 digits long")
elif num>=10000000 and num<100000000:
    print("This number is 8 digits long")
elif num>=100000000 and num<1000000000:
    print("This number is 9 digits long")
elif num>=1000000000 and num<10000000000:
    print("This number is 10 digits long")
else:    print("This number is more than 10 digits long")
