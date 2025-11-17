# List, Tuple, and Dictionary 
# List
# Sebuah tipe daya yang bisa menyimpan banyak nilai
myList = ["Jeruk", "Anggur", "Apel", 50000]
print(type(myList))
print(myList)
print(myList[1])
myList[0] = "Jeruk Bali" #Reassignment, overriding
print(myList)

#Tuple
# Data type yang mirip dengan List, namun bersifat imutable (tidak bisa dirubah)
myTuple = ("Jeruk Mandarin", "Anggur", "Apel", 50000)
print(type(myTuple))
print(myTuple)
print(myTuple[1])
# myTuple[0] = "Jeruk Bali" #Reassignment, overriding = Error
print(myTuple)

# Dictionary
#
import json
myDictionary = {
    "buah1": "Jeruk",
    "buah2": "Anggur",
    "buah3": "Apel",
    "harga": "50000"
}
print(type(myDictionary))
print(myDictionary)
print(myDictionary["buah2"])
myDictionary["buah1"] = "Jeruk Bali" # Can reassign new value to myDictionary
print(myDictionary)

#print biar rapi
print(json.dumps(myDictionary, indent=4))

#####################
## CHALLENGE TIME! ##
######################


