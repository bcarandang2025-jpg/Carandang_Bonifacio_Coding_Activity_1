# Create a shopping cart dictionary
cart = {'coffee': 2, 'cream': 5, 'soda': 1}

# Ask user for an item
item = input("Enter an item name: ").lower()

# Check if item exists in cart
if item in cart:
    cart[item] += 1
else:
    cart[item] = 1

# Print the cart in a readable format
print("\nYou have:", end=" ")

items = []
for name, count in cart.items():
    items.append(f"{count} {name}{'s' if count > 1 else ''}")

print(", ".join(items[:-1]) + ", and " + items[-1] + ".")

# Example output:
# Enter an item name: coffee
# You have: 3 coffee, 5 cream, and 1 soda.
