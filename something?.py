try:
    x=int(input("Enter a number."))
    import math
    print(math.ceil(x))
    print(math.floor(x))
    z=10
    a=z-25
    print("The value of z after copying the sign from a is: " + str(math.copysign(z,a)))
    y=int(input("Enter a secondary number."))
    print(math.fabs(x))
    print(math.fabs(x))
    print(math.gcd(x))
    print(math.sqrt(x or y))
    print(math.factorial(x or y))
    print(math.pow(x,y))
except TypeError:
    print("Do not use these integers." )
