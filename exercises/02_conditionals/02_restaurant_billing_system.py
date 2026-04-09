# This function will be tested automatically. 
# Do not change the function name or parameter.
def get_delivery_offer(bill_amount: float) -> str:
    # Write your code below this line
    if bill_amount > 500:
        return "You get a free dessert!"
    else:
        return "No free dessert this time."

amount = get_delivery_offer(250)
new_amount = get_delivery_offer(750)
print(amount)
print(new_amount)