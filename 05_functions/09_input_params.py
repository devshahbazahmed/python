# chai = "Ginger Chai"

# def prepare_chai(order):
#     print("Preparing", order)

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="high", milk="No") # keyword

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extra", extras)

special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="Yes")

# def chai_orders(order=[]):
#     order.append("Masala chai")
#     print(order)

def chai_orders(order=None):
    if order is None:
        order = []
        print(order)


chai_orders()
chai_orders()