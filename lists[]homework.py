
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))


squares = [i**2 for i in range(start, end + 1)]


oddsquares = [s for s in squares if s % 2 != 0]
evensquares = [s for s in squares if s % 2 == 0]
print(f"All Squares: {squares}")
print(f"Odd Squares: {oddsquares}")
print(f"Even Squares: {evensquares}")
