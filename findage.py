# wap to find the age including date , month and year when birth year is given

from datetime import datetime

def calculate_age(birth_date):
    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in years
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative months and days
    if days < 0:
        months -= 1
        days += (birth_date.replace(year=current_date.year , month=current_date.month) - birth_date.replace(year=current_date.year, month=current_date.month - 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Input birth date in YYYY-MM-DD format
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

# Get age in years, months, and days
years, months, days = calculate_age(birth_date)

print(f"You are {years} years, {months} months, and {days} days old.")