# This program can be used to calculate the volume of 5 different solids.

import math
pi = math.pi

print("Using this program, the volumes of the following solids can be calculated. ")
print(" 1) Cube \n 2) Cuboid \n 3) Sphere \n 4) Cylinder \n 5) Cone")


def vol_cube():
	
	# Function to calculate the volume of a cube given length of each side.
	
	length = float(input("Enter the length of sides of the cube : "))
	vol_of_cube = length ** 3
	print(vol_of_cube)


def vol_cuboid():
	
	# Function to calculate the volume of a cuboid given length of each side.
	
	length = float(input("Enter the length of the cuboid : "))
	breadth = float(input("Enter the breadth of the cuboid : "))
	height = float(input("Enter the height of the cuboid : "))
	vol_of_cuboid = length * breadth * height
	print(vol_of_cuboid)


def vol_sphere():
	
	# Function to calculate the volume of a sphere given radius.
	
	radius = float(input("Enter radius of the sphere : "))
	vol_of_sphere = (4 / 3) * pi * (radius ** 3)
	print(vol_of_sphere)


def vol_cylinder():
	
	# Function to calculate the volume of a cylinder given its radius and height.
	
	radius = float(input("Enter radius of the cylinder : "))
	height = float(input("Enter the height of the cylinder : "))
	vol_of_cylinder = pi * radius ** 2 * height
	print(vol_of_cylinder)


def vol_cone():
	
	# Function to calculate the volume of a cone given its radius and height.
	
	radius = float(input("Enter radius of the cone : "))
	height = float(input("Enter the height of the cone : "))
	vol_of_cone = pi * radius ** 2 * (height / 3)
	print(vol_of_cone)


def main():
	
	# Main function.
	# Accept the shape whose volume needs to be computed.
	# If incorrect input is entered, error message is printed and correct input is requested.
	# Once the volume of the solid is computed, check to see if volume needs to be computed again.
	
	shape = int(input("Enter the corresponding number to select the shape : "))
	if shape == 1:
		vol_cube()
	elif shape == 2:
		vol_cuboid()
	elif shape == 3:
		vol_sphere()
	elif shape == 4:
		vol_cylinder()
	elif shape == 5:
		vol_cone()
	c = int(input("Do you wish to try again? Enter 1 for yes or 0 for no : "))
	if c == 1:
		main()
	else:
		print("Thank you!")


if __name__ == "__main__":
 
	main()

