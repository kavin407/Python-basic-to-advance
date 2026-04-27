a={
"Name":"Adam",
"country":"india",
"Students":["Adam", "Rakesh"]
}
print(a.keys())
print(a.values())
print(a.items())
print(a.get("Name"))
#lets see what happens if we try to access a key that is not present 
# in the dictionary
print(a.get("Age"))
#we get None as the output because there is no key called "Age" 
# in the dictionary
