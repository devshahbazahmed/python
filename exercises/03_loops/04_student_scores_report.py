# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    result = []
    for name, score in zip(names, scores):
        result.append(f"{name} scored {score} marks")
    return result

print(generate_score_report([], []))
print(generate_score_report(["Riya", "Ramesh", "Suresh", "Bala"], [80, 65, 39, 50]))
print(generate_score_report(["Riya", "Ramesh", "Suresh", "Bala"], [80, 65, 39]))