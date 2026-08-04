#Local variable is a variable that is defined within a function and can only be accessed within 
# that function.
def order():
    food="Chicken rice"
    print("you're order is:",food)
    
order()    
print(food) # this will give an error because the 
#variable food is only defined within the function order() and cannot be accessed outside of it.