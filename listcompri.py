x=int(input("Enter a number: "))
oddnumbers=[num for num in range(x) if num%2!=0]
print(oddnumbers)


y=["orange", "apple", "banana", "kiwi", "cherry"]
firstletters = [word[0].upper() + word[1:] for word in y]
print(firstletters)
