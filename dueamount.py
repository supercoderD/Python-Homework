answer=float(input("Enter the bill you are paying."))
dueamount=int(input("Enter the dueamount."))
if dueamount > answer:
    difference = dueamount - answer
    print(f"You did not enter enough money to pay the due amount. You are short by:{difference}")
else:
    print("Payment accepted.")
