class Dog:
    animal="dog"
    def __init__(self, breed, color):
        self.breed=breed
        self.color=color

dog1=Dog("Husky", "black and white")
dog2=Dog("Golden Retriever", "Golden-Yellow")
dog3=Dog("Dalmatian", "black and white")
print("My dog is a ", dog1.breed, "and it is", dog1.color, "in color.")
print("My second dog, which is a", dog2.breed, "and is", dog2.color, "in color.")
print("My third dog, which is a ", dog3.breed, "and is ", dog3.color, "in color.")
        
    
