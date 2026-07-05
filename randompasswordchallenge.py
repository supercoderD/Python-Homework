import string
string.ascii_lowercase
string.ascii_uppercase
string.digits
print(string.ascii_lowercase+string.ascii_uppercase+string.digits)
import random
allchars=string.ascii_uppercase, string.digits, string.ascii_lowercase
a=""
for i in range(1,9):
    a+=random.choice(allchars)
print(a)
   


