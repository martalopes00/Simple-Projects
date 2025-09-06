# Ask the user for the product price
price = float(input('What is the product price?: '))

# Calculate the price with a 5% discount and show the result
print('With a 5% discount, the product costs {}'.format(price - (price * 0.05)))
