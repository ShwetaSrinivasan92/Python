# This program counts the total number of vowels in a given string.


def vowel_count(s):
	
	# Function to count number of vowels.
	# The vowels are initialised into a list.
	# Variable count initialised to 0 and incremented when a vowel is encountered.
	
	vowels = ['a', 'e', 'i', 'o', 'u']
	count, i = 0, 0
	
	for c in s:
		m = c.lower()
		if m in vowels:
			count += 1
			
	print("Total number of vowels : ", str(count))
	

if __name__ == "__main__":
	
	print("This program counts the number of vowels in a given string.")
	string = input("Enter the string to be checked : ")
	vowel_count(string)
