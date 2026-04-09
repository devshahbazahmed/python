# This function will be tested by the evaluation system. Do not modify the function name or parameters.
def check_loan_eligibility(age: int, income: float) -> str:
    if age >= 21:
        if income >= 25000:
            return "Eligible for loan"
        else:
            return "Not eligible: Income too low"
    else:
        return "Not eligible: Age must be 21 or above"

customer_1 = check_loan_eligibility(20, 25000)
print(customer_1)
customer_2 = check_loan_eligibility(24, 25000)
print(customer_2)
customer_3 = check_loan_eligibility(27, 20000)
print(customer_3)