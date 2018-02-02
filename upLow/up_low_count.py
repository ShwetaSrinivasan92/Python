# This programs computes the number of lowercase and uppercase letters in a given string.


def up_low(s):
	
	# Initialise the number of lowercase and uppercase letters to 0
	
	low, up = 0, 0
	
	# Traverse through the string entered by the user.
	# Increment low or up by 1 when a lowercase or uppercase letter is encountered respectively.
	# Print message if character other than alphabet is encountered.
	
	for c in s:
		if c.islower():
			low = low + 1
		
		elif c.isupper():
			up = up + 1
		
		else:
			if c.isdigit():
				print("Digits encountered.")
			else:
				print("Characters other than number or alphabet encountered.")
	
	print("Total number of letters : ", low + up)
	print("Number of lowercase letters : ", low)
	print("Number of uppercase letters : ", up)


if __name__ == "__main__":
	
	print("This programs computes the number of lowercase and uppercase letters in a given string.")
	string = input("Enter the string : ")
	up_low(string)
