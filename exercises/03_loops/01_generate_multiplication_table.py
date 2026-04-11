# This function will be tested automatically. 
# Do not change the function name or parameter type.
def multiplication_table(number: int) -> list[str]:
    tables = []
    for i in range(1, 11):
        tables.append(f"{number} x {i} = {number * i}")
    return tables

print(multiplication_table(2))
print(multiplication_table(5))