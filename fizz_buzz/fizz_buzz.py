# This program is prints numbers from 1 to 100.
# Multiples of 3 and 5 are not printed.


def fizz_buzz():
	
	# Numbers from 1 to 100 are analysed and printed.
	# Multiples fo 3 are represented by the word Fizz.
	# Multiples fo 5 are represented by the word Buzz.
	# Multiples fo 3 and 5 are represented by the word FizzBuzz.
	
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)


if __name__ == "__main__":
	
	print("This program prints numbers from 1 to 100 with 3 exceptions.")
	print("1) For multiples of 3, the word Fizz is printed.")
	print("2) For multiples of 5, the word Buzz is printed.")
	print("3) For multiples of 3 and 5, the word FizzBuzz is printed.")
	fizz_buzz()