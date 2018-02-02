# This program prints the Fibonacci series for n numbers.

def fib(n):
 
	# Accept the number of Fibonacci series to be printed and iteratively calculate the series
	
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a + b
		print(a)


if __name__ == "__main__":
	
	print("This program prints the Fibonacci series for n numbers.")
	num = int(input("Enter the number until which Fibonacci sequence has to be generated : "))
	fib(num)