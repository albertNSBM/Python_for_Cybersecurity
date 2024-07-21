# Importing Modules 

import random
import string 

characters= string.ascii_letters+string.digits+string.punctuation
length=13

random_characters=[]

for i in range(length):
	random_character=random.choice(characters)
	random_characters.append(random_character)
Password= ''.join(random_characters)

print(Password)

 
