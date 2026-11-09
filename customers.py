"""ISM2411 Lab 11: Customer Dictionary & Lookup."""

# Reflection 1:
# In real work, I would use .get() when a field is optional or when I am not sure
# that a key exists. I would use bracket notation when a field is required, so a
# missing key immediately shows that the data needs to be fixed.
#
# Reflection 2:
# Building the sales summary reminds me of creating a PivotTable in Excel because
# both methods group data and total values by category. Python can be more useful
# for large datasets because the same code can process many records repeatedly
# without requiring the summary to be rebuilt by hand.


def print_heading(number, title):
    """Print a clear heading for each exercise."""
    print(f"\nExercise {number}: {title}")


# Exercise 1: One customer
print_heading(1, "One customer")
customer = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and add
print_heading(2, "Update and add")
customer["phone"] = "813-555-0147"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe lookup
print_heading(3, "Safe lookup")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError caught: {error}")


# Exercise 4: Iterate
print_heading(4, "Iterate")
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items() returns only the dictionary's keys, not its values.
print("Keys returned without .items():")
for key in customer:
    print(key)


# Exercise 5: Lookup table
print_heading(5, "Lookup table")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15,
}

purchase_amount = 200.00
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of dictionaries
print_heading(6, "List of dictionaries")
customers = [
    {"name": "Alice Johnson", "tier": "platinum"},
    {"name": "Bruno Silva", "tier": "gold"},
    {"name": "Carla Mendes", "tier": "silver"},
]

purchase_amount = 300.00
for current_customer in customers:
    tier = current_customer["tier"]
    rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_amount * rate
    print(
        f"{current_customer['name']} | Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )


# Exercise 7: Nested catalog
print_heading(7, "Nested catalog")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} has {product_details['stock']} units left")


# Exercise 8: Sales by region
print_heading(8, "Sales by region")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + transaction["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:,.2f}")
