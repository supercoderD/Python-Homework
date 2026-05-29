testdictionary={"Codingal": 3, "is" : 2, "for": 2, "Coding":1}
print("The original dictionary:" + str(testdictionary))
k=2
res=0
for key in testdictionary:
    if testdictionary[key]==k:
        res+=1

print("Frequency of k is:" + str(res))
