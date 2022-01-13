# Simple random password generator (8 chars long)

import random

# List for the uppercase characters
uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List for the lowercase characters
lowercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List for the numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List for the special characters
special_characters = ['!', '@', '#', '$', '%', '&', '?', '^', '+']

# Create a password adding randomly one item for each list from above
my_password = random.choice(uppercase_characters) * 2 + random.choice(lowercase_characters) * 2 + random.choice(numbers) * 2 + random.choice(special_characters) * 2

print(my_password)