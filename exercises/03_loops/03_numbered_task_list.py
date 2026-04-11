# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	final_list = []
	for idx, task in enumerate(tasks, start=1):
		final_list.append(f"{idx}. {task}")
	return final_list

print(generate_numbered_tasks([]))
print(generate_numbered_tasks(["Clean laptop", "Exercise", "Breakfast", "Coding", "Reading book"]))