#1
x=int(input("Enter a number : "))
if x%2==0:
    print("Your number is even.")
else:
    print("Your number is odd.")
#2
age=int(input("Enter a random age: "))
if age<13:
    print("Child.")
elif age<20 and age>=13:
    print("Tenager")
elif age>=20 and age<60:
    print("Adult")
else: 
    print("Senior")
#3
n=int(input("Enter a number")) 
for i in range(1, n + 1):
    cube = i ** 3
    print(f"The cube of {i} is {cube}")
#4
x=0
for i in range(1,51):
    if i%2==0:
        x+=i 
print("The sum of all even numbers from 1-50 is", x)
#5
n = 5  
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)



    





