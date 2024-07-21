# importing necessary library
import hashlib 
import os 
os.system('figlet Hashing Tool')
print()

# receriving string from user 

text=input('Enter the string to get hash :')
print()
# now let's encode the input 

encoded_text = text.encode() 

md5_hash = hashlib.md5(encoded_text).hexdigest()
sha1_hash = hashlib.sha1(encoded_text).hexdigest()
print(f'MD5 Hash: {md5_hash}')
print()
print(f'SHA1 Hash: {sha1_hash}')
