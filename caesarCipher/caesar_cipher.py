# This program implements the Caesar Cipher.


def caesar_cipher_encrypt():
	
	# Function to encrypt the message given by the user by implementing the key value specified.
	# Both lower case and upper case letters are taken into consideration.
	# Characters other than alphabets are ignored.
	
	message = input("Enter the string to be encrypted : ")
	key = int(input("Enter the key : "))
	for c in message:
		if c.isalpha() and c.islower():
			enc_ascii = (ord(c) - 97 + key) % 26 + 97
			print(chr(enc_ascii), end = '')
		if c.isalpha() and c.isupper():
			enc_ascii = (ord(c) - 65 + key) % 26 + 65
			print(chr(enc_ascii), end = '')
		if not c.isalpha():
			print(c)


def caesar_cipher_decrypt():
	
	# Function to decrypt the message given by the user by implementing the key value specified.
	# Both lower case and upper case letters are taken into consideration.
	# Characters other than alphabets are ignored.
	
	message = input("Enter the string to be decrypted : ")
	key = int(input("Enter the key : "))
	for c in message:
		if c.isalpha() and c.islower():
			enc_ascii = (ord(c) - 97 - key) % 26 + 97
			print(chr(enc_ascii), end = '')
		if c.isalpha() and c.isupper():
			enc_ascii = (ord(c) - 65 - key) % 26 + 65
			print(chr(enc_ascii), end = '')
		if not c.isalpha():
			print(c)


def main():
	choice = int(input("\nOptions : \n 1) Encrypt \n 2) Decrypt \n Your choice : "))
	if choice == 1:
		caesar_cipher_encrypt()
	elif choice == 2:
		caesar_cipher_decrypt()
	c = int(input("\nDo you wish to try again? Enter 1 for yes or 0 for no : "))
	if c == 1:
		main()
	else:
		print("Thank you!")


if __name__ == "__main__":
	
	print("This program is used to implement the Caesar Cipher.")
	print(
		"Caesar cipher can be used to encrypt any alphabetic string by shifting the letters by a specified value/key.")
	print("This is the simplest form of encryption said to have been introduced by Julius Caesar.")
	print("No security is provided since it is very easy to break a Caesar Cipher.")
	main()
