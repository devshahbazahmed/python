# This function will be tested automatically. 
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    messages = []
    i = 0
    while i < len(withdrawals):
        amount = withdrawals[i]
        
        if (balance >= amount):
            balance -= amount
            messages.append(f"Withdrawal: {amount}")
        else:
            messages.append(f"Insufficient funds for requested amount: {amount}")
        
        i += 1

    messages.append(f"Remaining Balance: {balance}")
    return messages

print(simulate_atm_withdrawals(1000, [100, 200, 300, 400, 500]))