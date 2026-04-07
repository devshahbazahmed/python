# branch_a_products = {"bread", "milk", "butter", "jam"}
# branch_b_products = {"bread", "cheese", "butter", "ketchup"}

# print(branch_a_products)
# print(branch_b_products)

# print(branch_a_products.union(branch_b_products))

# print(branch_a_products.intersection(branch_b_products))

# print(branch_a_products.difference(branch_b_products))

# print("ketchup" in branch_a_products)

# essential_items = frozenset(["milk", "bread", "ketchup"])
# print(essential_items)

branch_a_products = {"bread", "milk", "butter", "jam"}

branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(branch_a_products)
print(branch_b_products)

all_branches = branch_a_products | branch_b_products
print(all_branches)

common_products = branch_a_products & branch_b_products
print(common_products)

only_in_branch_a = branch_a_products - branch_b_products
print(only_in_branch_a)

print("ketchup" in branch_a_products)

essential_items = frozenset(["milk", "bread", "ketchup"])
print(essential_items)