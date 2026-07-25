class PIN:
    __pin=4922
    def __init__(self, owner, pin):
        self.owner=owner
        self.__pin=pin
    def pinstatus(self):
        print("The account owner is", self.owner)
        print("PIN is secured inside of the account.")
    def setpin(self, newpin):
        if len(newpin)==4 and newpin.isdigit():
            self.__pin= newpin
            print("PIN has been updated sucessfully. Congratulations.")
        else:
            print("Your PIN must consist of numbers only. Please change your PIN.")

    def checkpin(self, enteredpin):
        if enteredpin==self.__pin:
            print("Access granted.")
        else:
            print("Acess denied.")

    def __str__(self):
        return "The account holder is:"+ self.owner

account=PIN("Darsh", 4922)

print(account)

account.pinstatus()
account.__pin="8741"
print("We tried changing the PIN from outside.")
account.checkpin("8741")
account.checkpin("4922")
account.setpin("8741")
account.checkpin("8741")









