# Ask the user for the width of the wall
width = float(input('What is the width of your wall in meters?: '))

# Ask the user for the height of the wall
height = float(input('What is the height of your wall in meters?: '))

# Calculate the area of the wall and the amount of paint needed (1 liter for every 2 m²)
print('The area of the wall is {} m² and you need {} liters of paint to cover it.'.format(width * height, (width * height) / 2))
