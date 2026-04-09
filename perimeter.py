length=int(input("Enter the length for the rectangle/square"))
width=int(input("Ente the width for the rectangle/square"))
perimeter=(2*length)+(2*width)
if length==width:
    print("The perimeter of this square is: " , perimeter)
else:
    print("The perimeter of this rectange is: " , perimeter)
answerforarea=input("Do you want the area of this square?")
if answerforarea=="yes" or "YES":
    area=length*width
    print("The area of the polygon is: ", area)
