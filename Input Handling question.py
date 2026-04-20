# Description
# A school wants to create a simple 
# program to evaluate a student’s performance based on marks obtained in five subjects: Maths,
#  Science, Social, English, and Tamil.
print("Enter the marks for each subject:")
Maths=int(input("Enter the maths marks: "))
Science=int(input("Enter the science marks: "))
Social=int(input("Enter the social marks: "))   
English=int(input("Enter the english marks: "))
Tamil=int(input("Enter the tamil marks: "))
Total = Maths + Science + Social + English + Tamil
Average = Total / 5
if Average < 35:
    print("Additional Classes Needed")
else:
    print("You are good to go!")