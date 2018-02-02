# This program calculates the number of tiles required to cover a room floor and its corresponding cost.


def cost_of_tile(ra, ta, cost):
	
	# Number of tiles necessary is computed by dividing the area of room by the area of each tile.
	# Total cost of tiles is calculated by multiplying number of tiles with the cost of each tile.
	
	number_of_tiles = ra / ta
	cost_of_tiles = number_of_tiles * cost
	print('Total number of tiles required to cover the room is ' + str(number_of_tiles))
	print('The corresponding cost is ' + str(cost_of_tiles))


def main():
	
	# Main function
	# Length and breadth of the room is accepted from the user and area of the room is computed.
	# Length and breadth of each tile is accepted from the user and area of a single tile is computed.
	# Cost of each tile is accepted from the user.
	
	print("This program can be used to calculate the total number and the cost of tiles required to cover a room floor.")
	
	room_length = float(input("Enter the length of the room in feet : "))
	room_breadth = float(input("Enter the breadth of the room in feet : "))
	room_area = room_length * room_breadth
	
	tile_length = float(input("Enter the length of the tile in feet : "))
	tile_breadth = float(input("Enter the breadth of the tile in feet : "))
	tile_area = tile_length * tile_breadth
	
	cost = float(input("Enter the cost of each tile : "))
	
	cost_of_tile(room_area, tile_area, cost)


if __name__ == "__main__":
	main()
