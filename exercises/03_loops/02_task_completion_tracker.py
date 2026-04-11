# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    updated_tasks = []
    for task in tasks:
        updated_tasks.append(f"Completed: {task}")
    return updated_tasks

print(mark_completed_tasks([]))
print(mark_completed_tasks(["Clean laptop", "Exercise", "Breakfast", "Coding", "Reading book"]))