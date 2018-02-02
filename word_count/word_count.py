# This program gives the count of number of lines, words and letters in a given file.


def word_count(s):
	
	# Function that counts the number of lines words and letters.
	# If file is empty, error message is printed.
	# To count the number of lines, the input data from file is split when a new line character is encountered.
	# To count the number of words, the input data from file is split when a space is encountered.
	# To count the number of letters, the input data is traversed and count is incremented whenever an alphabet is encountered.
	
	letter = 0
	
	if len(s) == 0:
		print("File is empty")
		
	else:
		lines = s.split("\n")
		words = s.split(" ")
		print(words)
		for c in s:
			if c.isalpha():
				letter += 1
		print("Number of lines in the file are : " + str(len(lines)))
		print("Number of words are : " + str(len(words)))
		print("Number of letters are : " + str(letter))


def main():
	
	# Main function.
	# Accepts the filename from user and reads from file.
	# If given filename does not exist, error message is printed.
	
	try:
		print("This program gives the count of number of lines, words and letters in a given file.")
		filename = input("Enter the name of input file : ")
		with open(filename, "r") as f:
			data = f.read()
			word_count(data)
	except IOError:
		print("File not found.")


if __name__ == "__main__":
	
	main()
