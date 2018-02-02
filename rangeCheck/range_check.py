# This program can be used to check if a given number lies within a specified range of numbers.


def range_check(n, l, h):
 
	# Compare if the number specified lies between the low and high values mentioned by the user.
	# Chained comparison operator is used to verify this.
	# Appropriate message is printed.
	
	if l <= n <= h:
		print("The entered number lies within the range specified")
	
	else:
		print("The number does not lie within the range specified")


if __name__ == "__main__":
	
	print("This program can be used to check if a given number lies within a specified range of numbers.")
	num = float(input("Enter the number to be verified : "))
	low = float(input("Enter the lowest number in the range to be verified : "))
	high = float(input("Enter the highest number in the range to be verified : "))
	range_check(num, low, high)
