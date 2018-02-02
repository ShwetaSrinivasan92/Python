# This program check to verify if the given string is a palindrome or not.


def palindrome(string):

	# Function to check if the string is a palindrome or not.
	# The given string is reversed and stored in the variable reverse.
	# The string provided and its reverse are compared.
	# If they are the same, then the string is a palindrome. Else, it is not.
	
	s = string.replace(" ", "")
	reverse = s[::-1]
	if s == reverse:
		print("The given string \"" + string + "\" is a palindrome.")
	else:
		print("The given string \"" + string + "\" is not a palindrome.")


def main():
	
	# Main function that accepts the string to be verified.
	
	print("This program check to verify if the given string is a palindrome or not.")
	string = input("Enter the string to be verified : ")
	palindrome(string)


if __name__ == "__main__":
	
	main()
