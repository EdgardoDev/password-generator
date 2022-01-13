# This is a simple password generator that will use words from an external file.

import random

wordlist = []
# List for the special characters
special_characters = ['!', '@', '#', '$', '%', '&', '?', '^', '+']

with open("article.txt", "r") as file:
  data = file.readlines()
  
  # Loop through each line
  for line in data:
    # Split lines into words
    words = line.split()
    # Select an element inside wrds and add a condition to add only words > 5 to the wordlist.
    for item in words:
      if len(item) > 5:
        wordlist.append(item.capitalize()) # Capitalize each word
        
        
random_word = random.choice(wordlist)
special_character = random.choice(special_characters)
numbers = str(random.randint(10, 99))

readable_password = random_word + special_character + numbers

print(readable_password)