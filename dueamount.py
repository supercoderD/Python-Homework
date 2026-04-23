dueamount=float(input("Enter the total bill."))
bill=float(input("Enter how much you pay the shopkeeper."))
answer=bill-dueamount
if dueamount>0:
    print("You did not enter enough money to pay the due amount.")
if dueamount<=0:
    print("The shopkeeper will pay you", answer)