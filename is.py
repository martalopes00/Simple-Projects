# Ask the user to type something
something = input('Type something: ')

# Show the primitive type of the input
print('The primitive type of this value is', type(something))

# Check if it contains only spaces
print('Only spaces?', something.isspace())

# Check if it is numeric
print('Is it a number?', something.isnumeric())

# Check if it is alphabetic
print('Is it alphabetic?', something.isalpha())

# Check if it is uppercase
print('Is it uppercase?', something.isupper())

# Check if it is lowercase
print('Is it lowercase?', something.islower())

# Check if it is capitalized (title case)
print('Is it capitalized?', something.istitle())
