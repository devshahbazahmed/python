# String

chai_type = "Ginger Chai"
customer_name = 'Priya'

print(f"Order for: {customer_name} : {chai_type} please")

chai_description = "Aromatic and Bold more"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

label_text = "Chai Special"

encoded_label = label_text.encode("utf-8")
print(f"Encoded Label: {encoded_label}")
print(f"Non-encoded Label: {label_text}")

decoded_label = encoded_label.decode("utf-8")