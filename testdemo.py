# Variables and data types
greeting = "Hello, Python world!"
user_score = 95
is_active = True

print(greeting)

# Working with Lists
favorite_fruits = ["Apple", "Banana", "Lime"]
print(f"Original list: {favorite_fruits}")

# Add an item to the end of a list
favorite_fruits.append("Mango")

# Loop through a list with index tracking
for index, fruit in enumerate(favorite_fruits):
    print(f"Fruit {index + 1}: {fruit}")

# Simple conditional checks
if user_score >= 90 and is_active:
    print("Status: Top active performer!")
