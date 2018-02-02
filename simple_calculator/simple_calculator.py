# This program works as a simple calculator


def simple_calc(a, op, b):
	
	# Checks if the operator entered is among +, -, * or /
	if op not in '+-*/':
		return "Please select valid operators : +, -, * or /"
	
	# Performs addition with the operands entered
	if op == '+':
		return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a+b)
	
	# Performs subtraction with the operands entered
	if op == '-':
		return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a-b)
	
	# Performs multiplication with the operands entered
	if op == '*':
		return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a*b)
	
	# Performs division with the operands entered
	if op == '/':
		try:
			return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a/b)
		except ZeroDivisionError:
			return 'Divide by zero error'
			

def main():
	
	# Main function that accepts 2 operands and 1 operator
	
	print("This program works as a simple calculator.")
	a = float(input("Enter the first operand : "))
	op = input("Enter the operation to be performed. Choose between +, -, * or / : ")
	b = float(input("Enter the second operand : "))
	print(simple_calc(a, op, b))
	

if __name__ == "__main__":
	
	main()
