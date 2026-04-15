class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    

class ChaiUtils:
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
print(ChaiUtils.is_valid_size("Medium"))

order_one = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "medium", "size": "large"})
print(order_one.__dict__)
order_two = ChaiOrder.from_string("Ginger-Low-Small")
print(order_two.__dict__)
order_three = ChaiOrder("Large", "Low", "Large")
print(order_three.__dict__)