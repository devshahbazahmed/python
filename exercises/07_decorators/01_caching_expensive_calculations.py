# This function will be tested automatically.
# Do not change the function name or parameters.


def cache_results(func):
    # Write your code below this line
    cache = {}
    def wrapper(*args):
        if args in cache:
            return f"From Cache: {cache[args]}"
        else:
            result = func(*args)
            cache[args] = result
            return f"Computed: {result}"
    return wrapper

@cache_results
def multiply(a: int, b: int) -> int:
    return a * b