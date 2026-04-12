loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    total = 0
    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50

    for amount in transactions:
        total += amount
    apply_bonus()
    global loyalty_points
    loyalty_points += total // 100
    print(loyalty_points)
    return total

print(loyalty_points)
print(process_transactions([100, 200, 300 ,400]))