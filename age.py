from datetime import datetime
dob = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob, "%Y-%m-%d")

today = datetime.now()
age = today.year - dob.year
if today.month < dob.month:
    age -= 1
elif today.month == dob.month and today.day < dob.day:
    age -= 1

print(f"You are {age} years old.")
