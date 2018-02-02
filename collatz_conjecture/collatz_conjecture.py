# This program emulates the Collatz Conjecture.
# The assumption is that no matter what positive integer we begin with, the sequence always reaches 1.


def collatz_conjecture(n):
	
	# Function that implements the Collatz Conjecture.
	# Until n = 1,
	# If n is even, divide by 2.
	# Else, multiply n by 3 and add 1.
	
	while n != 1:
		
		if n % 2 == 0:
			n /= 2
			
		else:
			m = 3 * n
			n = m + 1
		
		print(n)


def main():
	
	# Main function.
	# Accepts a positive integer from the user
	
	print("This program emulates the Collatz Conjecture.")
	integer = int(input("Enter a positive integer : "))
	collatz_conjecture(integer)


if __name__ == "__main__":
	
	main()
