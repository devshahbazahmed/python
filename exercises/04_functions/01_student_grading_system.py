def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score < 90 and score >= 75:
        return "B"
    elif score < 75 and score >= 60:
        return "C"
    elif score < 60 and score >= 40:
        return "D"
    else: 
        return "F"
        

def generate_student_report(name, score):
    grade = calculate_grade(score)
    return f"{name} has scored {score} and received grade {grade}"

report_1 = generate_student_report("Aman", 45)
print(report_1)
report_2 = generate_student_report("Riya", 98)
print(report_2)
report_3 = generate_student_report("Sushant", 72)
print(report_3)