#Enclosing variable is a variable that is defined within a function and can be accessed by the
#  inner function.
def card():
    discount=10
    def checkout():
        print("you have a disscount of:",discount,"%")
    checkout()
card()