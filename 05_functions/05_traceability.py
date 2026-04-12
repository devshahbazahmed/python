def add_vat(price, vat_percent):
    return price * (100 + vat_percent) / 100

orders = [100, 250, 360]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Price: {price}, Final amount after VAT: {final_amount}")