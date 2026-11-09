"""Practice variables, input, type conversion, and print."""

name = input("What is your name? ").strip()
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(f"Hello, {name}!")
print(f"{first_number:g} + {second_number:g} = {first_number + second_number:g}")
