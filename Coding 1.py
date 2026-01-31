# Ask the user for their name and age, then store the inputs in variables.
import string


name = input("Enter your name: ")
age = int(input("Enter your age: "))

# calculate age next year
next_year_age = age + 1
next_year_age_str = str(next_year_age)

# print the greeting message
print(f"Hello, {name}! Next year, you will be {next_year_age_str} years old.")

 # Optional: show the length of the name
name_length = len(name)
print(f"Your name has {name_length} characters.")
