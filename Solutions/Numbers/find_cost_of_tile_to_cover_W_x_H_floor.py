"""
**Find Cost of Tile to Cover W x H Floor** - Calculate the total cost
of tile it would take to cover a floor plan of width and height,
using a cost entered by the user.
"""

tile_cost = 7

print("What is the width and height of the floor?")
width = int(input("Width: "))
height = int(input("Height: "))

print("Total cost to cover the floor is {} dollars.".format(width*height*tile_cost))
