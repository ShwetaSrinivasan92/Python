# This program prints out the Pascal's triangle up to the specified level.


def pascal(n):
	
	# Initialise val to 1 as the Pascal's triangle begins from 1
	val = 1
	
	# If only 1 level has to be printed, return 1.
	# Else, calculate the numbers in each level of the triangle and print.
	
	if n == 1:
		return 1
	
	else:
		for i in range(0, n):
			for j in range(0, i + 1):
				if i == 0 or j == 0:
					val = 1
				else:
					val = val * (i - j + 1) / j
				print(int(val), end = " ")
			print()


if __name__ == "__main__":
 
	print("This program prints out the Pascal's triangle up to the specified level.")
	num = int(input("Enter the level of Pascal triangle to be printed : "))
	pascal(num)