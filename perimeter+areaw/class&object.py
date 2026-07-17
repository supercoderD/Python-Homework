class rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def perimeter(self):
        return 2*(self.length+self.width)
    def area(self):
        return (self.length*self.width)
userinput=int(input("Enter the length of the rectangle:"))
userinput2=int(input("Enter the width of the rectangle:"))
myrectangle=rectangle(userinput, userinput2)
areaforrectangle=myrectangle.area()
perimterforrecangle=myrectangle.perimeter()
print("The area of the rectangle is:", areaforrectangle)
print("The perimter for the rectangle is:", perimterforrecangle)