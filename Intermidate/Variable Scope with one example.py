
def hotel(): 
    item="pizza"
    def order_now():
        quantity=2
        delivery_partner="ABC company"
        print(f"ORDERING {quantity} {item} from {delivery_partner}")
    order_now()
hotel()