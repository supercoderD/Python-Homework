birthday1=input("What is your birthday?: ")
birthday2=input("What is your friend's birthday?: ")
if birthday1==birthday2:
    print("You share the same birthday!")
else:
    print("You have different birthdays.")
    birthday3=input("When is your other friend's birthday?: ")
    if birthday1==birthday3 or birthday2==birthday3:
        print("You share a birthday with one of your friends!")
    else:
        print("All three of you have different birthdays.")
        birthday4=input("When is another of your friend's  birthday?: ")
        if birthday1==birthday4 or birthday2==birthday4 or birthday3==birthday4:
            print("You share a birthday with one of your friends!")
        else:
            print("All four of you have different birthdays.")  
            birthday5=input("When is your last friend's  birthday?: ")
            if birthday1==birthday5 or birthday2==birthday5 or birthday3==birthday5 or birthday4==birthday5:
                print("You share a birthday with one of your friends!")
            else:
                print("All five of you have different birthdays.")
            print("Thanks for using the birthday checker!")