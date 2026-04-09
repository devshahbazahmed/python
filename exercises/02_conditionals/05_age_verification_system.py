# This function will be tested automatically. 
# Do not change the function name or parameter type.
def verify_age(age_str: str) -> str:
    # Write your code here
    age = int(age_str)
    if age >= 18:
        return "Access Granted"
    else:
        return "Access Denied"

person_1 = verify_age(10)
print(person_1)
person_2 = verify_age(20)
print(person_2)