# The purpose of this program is to count how many weeks you have left if you live until 90.
MAX_AGE = 90
YEAR = 52
age = int(input("Please provide your age: "))

years_left = MAX_AGE - age
weeks_left = years_left * YEAR

print(f"You have {weeks_left} weeks left.")
