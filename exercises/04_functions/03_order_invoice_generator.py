def generate_invoice(customer_name="Guest", *items, **charges):
    lines = []
    
    # Header
    lines.append(f"Invoice for {customer_name}:")
    
    # Items-section
    if items:
        lines.append(f"Items:")
        for item in items:
            lines.append(f"- {item}")
    
    # Charges-section
    total = 0.0
    if charges:
        lines.append(f"Charges:")
        for name, amount in charges.items():
            capitalized_name = name.capitalize()
            lines.append(f"{capitalized_name}: {amount}")
            total += amount
            
    # Total-section
    lines.append(f"Total Amount Due: {total}")
    
    return "\n".join(lines)

print(generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0))
print(generate_invoice("Riya", tax=30.0))
print(generate_invoice())
print(generate_invoice("John", "Pizza", "Coke"))