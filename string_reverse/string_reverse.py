# This program prints the reverse of a given string.


def reverse(s):
	
	# Function to print the reverse of a given string.
	
	st = " "
	
	# Length of entered string is checked
	# If length is 0, error message is printed.
	# Else, the string is reversed iteratively.
	
	if len(s) == 0:
		return 'No string entered.'
	
	else:
		for c in s:
			st = c + st
		return st


def main():
	
	# Main function that accepts the string to be verified.
	
	print("This program prints the reverse of a given string.")
	string = input("Enter the string to be reverse : ")
	print(reverse(string))


if __name__ == "__main__":
	
	main()
