# This function will be tested automatically.
# Do not change the function name or parameter type.
def get_item_price(item: str) -> str:
    # write your code below this line
    item = item.lower()
    match item:
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"

item_1 = get_item_price("Burger")
print(item_1)
item_2 = get_item_price("PiZZa")
print(item_2)
item_3 = get_item_price("Juice")
print(item_3)