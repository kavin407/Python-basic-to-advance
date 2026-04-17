# Global Variable is a variable that is defined outside of any function and can be accessed
#  by any function in the program.
user_id="Adam"
def homepage():
    print("Welcome to the homepage",user_id)

def profile():
    print("Welcome to your profile",user_id)

homepage()
profile()