# Importing Modules 
import os
os.system('figlet Pass Generator Tool')

import random
import string 

# Generating  a string where the automated pass will be generated 
characters= string.ascii_letters+string.digits+string.punctuation
length=13

random_characters=[]   # list that wil help us to store generated password 

for i in range(length):           # loop for generating password
	random_character=random.choice(characters)
	random_characters.append(random_character)
Password= ''.join(random_characters)            # using join() to join the character in the list

print(Password)

 
