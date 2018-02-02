# This program accepts the total cost of items purchased and the amount paid and calculates the change to be returned.
# The number of quarters, dimes, nickles and pennies to be returned is printed.

def change_calculator(n):
 
	# Initialise the value of quarter, dime, nickle and penny respectively.
	# Compute the change remaining after each of the above currency is deducted.
	# Print the values.
	
	quarter = .25
	dime = .10
	nickel = .05
	penny = .01
	
	qB = change // quarter
	qBalance = change - qB * quarter
	dB = qBalance // dime
	dBalance = qBalance - dB * dime
	nB = dBalance // nickel
	nBalance = dBalance - nB * nickel
	pB = nBalance // penny
	pBalance = nBalance - pB * penny
	
	print("Change to be returned : ")
	print(str(qB) + " quarters")
	print(str(dB) + " dimes")
	print(str(nB) + " nickels")
	print(str(pB) + " pennies")


if __name__ == "__main__":
 
	print("Given the cost of items purchased and the amount paid, this program calculates the change to be returned "
	      "and also gives the number of each type of coin to be used")
	cost = float(input("Enter the cost of the items purchased : "))
	amount = float(input("Enter the amount paid by the customer : "))
	change = cost - amount
	change_calculator(change)
