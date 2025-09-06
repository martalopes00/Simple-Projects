# Ask the user how much money they have
money = float(input('How many euros do you have? '))

# Set the dollar exchange rate
dollar = 1.17

# Calculate how many dollars the user can buy
print(f'You can buy {money * dollar} dollars.')
