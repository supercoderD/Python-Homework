ask=int(input("Enter a number that is not a decimal or fraction.: "))
ask2=int(input("Enter another number that is not a decimal or fraction.: "))
ask3=int(input("Enter another number that is not a decimal or fraction.: "))
def add(ask, ask2, ask3):
    return ask+ask2+ask3
def subtract(ask, ask2, ask3):
    return ask-ask2-ask3
def multiply(ask, ask2, ask3):
    return ask*ask2*ask3
def divide(ask, ask2, ask3):
    return ask/ask2/ask3
def exponent(ask, ask2, ask3):
    return ask**ask2
userorperation=input("Enter the operation you want.")
if userorperation=="+":
    print(add(ask, ask2, ask3))
elif userorperation=="-":
    print(subtract(ask, ask2, ask3))
elif userorperation=="*":
    print(multiply(ask, ask2), ask3)
elif userorperation=="/":
    print(divide(ask,ask2, ask3))
elif userorperation=="**":
    print(exponent(ask, ask2, ask3))
else:
    print("This is an invalid input. ")



n=int(input("Enter a number"))
for i in range(n):
    n+=1
print (n)