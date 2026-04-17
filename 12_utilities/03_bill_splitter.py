"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def get_total_bill(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

num_people = int(input("Enter the number of people: ").strip())
names = []

for i in range(num_people):
    name = input(f"Enter the name of person #{i+1}: ").strip()
    names.append(name)

print(names)

total_bill = get_total_bill("Enter the total bill amount: ")

share = round(total_bill / num_people, 2)

print("\n" + "*" * 40)
print(f"Total Bill: {total_bill}")
print(f"Each person owes: {share}")

for name in names:
    print(f"{name} owes {share}")

print("\n" + "*" * 40)


