# This program is used to convert a given English string into its corresponding Pig Latin string.


def pig_latin(s):
	
	# Function that converts a given English string into Pig Latin.
	# Initial check done to compute length of string. If length = 0, error message is printed.
	# Else, the string is split into words and output is printed.
	
	if len(s) == 0:
		print("No string entered.")
		
	else:
		words = s.split(" ")
		for c in words:
			strng = c[1:]
			init = c[0]
			pl = strng + init + 'ay'
			print(pl)


def main():
	
	# Main function.
	# Accepts the string from user.
	
	print("This program is used to convert a given English string into its corresponding Pig Latin string.")
	
	string = input("Enter the string you wish to convert : ")
	pig_latin(string)


if __name__ == "__main__":
	
	main()
