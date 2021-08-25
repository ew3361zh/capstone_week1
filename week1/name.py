"""
Program that asks user for name and bday month.
Calculates name length, greets user, and checks if the current month is their birthday month
"""

# ask for name using input, store in variable
name = input("What is your name? ")
# same for birthday month
birthday_month = input("What month were you born in? ")
# print hello message using name variable info
print(f'Hello, {name}, so nice to meet you!')
# print number of letters using
print(f'You have {len(name)} letters in your name')
if birthday_month.lower() == 'august':
    print('Happy birthday month to you!')

from time import strftime
current_month = strftime('%B')

if current_month.lower() == birthday_month.lower():
    print('it\'s currently your birthday month!')