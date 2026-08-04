age=int(input("Enter your age: "))
has_license=input("Do you have a driving license? (yes/no): ").lower()
if age>=18:
    if has_license=="yes":
        print("You can go")
    else:
        print("You  go and get a driving license")
else:
    print("You cannot go")
