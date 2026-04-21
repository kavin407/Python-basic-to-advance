order_amount=1000
day="saturday"
membership="no"
if (order_amount>=1000 and day=="saturday") or membership=="gold":
    print("You have 20% discount")
else:
    print("No discount for you")