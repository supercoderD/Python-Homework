a = 10
b = 20
c = 30

# This rotates the values: a gets b, b gets c, c gets a
a, b, c = b, c, a

print(f"a: {a}, b: {b}, c: {c}") 
# Output: a: 20, b: 30, c: 10
