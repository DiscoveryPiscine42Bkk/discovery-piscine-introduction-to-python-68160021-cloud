
try:
    current_age = int(input("Please tell me your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number for your age.")
    exit(1)


age_in_10 = current_age + 10
age_in_20 = current_age + 20
age_in_30 = current_age + 30


print(f"You are currently {current_age} years old.")
print(f"In 10 years, you'll be {age_in_10} years old.")
print(f"In 20 years, you'll be {age_in_20} years old.")
print(f"In 30 years, you'll be {age_in_30} years old.")