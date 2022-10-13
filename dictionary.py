myDictionary={
    "bhoomi":"land",
    "prani":"animal",
    "ane":"elephant",
    "jinke":"deer"
}
print("options are",myDictionary.keys())
b=input("Enter the kannada word\n")
print("The meaning of the word:",myDictionary[b])
print("The meaning of the word:",myDictionary.get(b))
