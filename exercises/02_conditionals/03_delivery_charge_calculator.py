# This function will be tested automatically. 
# Do not change the function name or parameter type.
def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance > 2 and distance <= 5:
        return "Delivery charge: 30"
    elif distance > 5 and distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."

delivery_charge_1 = calculate_delivery_charge(5)
print(delivery_charge_1)
delivery_charge_2 = calculate_delivery_charge(2)
print(delivery_charge_2)
delivery_charge_3 = calculate_delivery_charge(8)
print(delivery_charge_3)
delivery_charge_4 = calculate_delivery_charge(12)
print(delivery_charge_4)