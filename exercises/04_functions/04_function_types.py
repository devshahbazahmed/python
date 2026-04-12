# Pure Function
def pure_add(a, b):
    return a + b

# Impure Function
counter = 0
def impure_increment():
    global counter
    counter += 1
    return counter
    
# Recursive Function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    result = n * factorial_recursive(n - 1)
    return result

# Lambda Function
def square_list(nums):
    new_nums = list(map(lambda n: n**2, nums))
    return new_nums