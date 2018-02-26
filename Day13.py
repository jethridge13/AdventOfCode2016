import unittest

def calc(coords, fav, pos=[1, 1]):
	# TODO Dynamically generate grid, then Dijkstra's
	# Generate a grid of dimensions twice the size of target coords
	# Does not guarantee a solution every time for odd inputs,
	# but will be good enough for the problem.
	grid = generateGrid(coords, fav)
	grid[pos[1]][pos[0]] = 0
	coordsToCheck = [pos]
	while grid[coords[1]][coords[0]] == '.':
		newCoords = []
		for i in coordsToCheck:
			newCoords += checkSurroundingCoords(i, grid)
		coordsToCheck = newCoords
	return grid[coords[1]][coords[0]]

def checkSurroundingCoords(coords, grid):
	# TODO Still very buggy
	validSpots = []
	if not coords:
		return validSpots
	if coords[0]-1 >= 0 and grid[coords[0]-1][coords[1]] == '.':
		validSpots.append([coords[1], coords[0]-1])
	if coords[1]-1 >= 0 and grid[coords[0]][coords[1]-1] == '.':
		validSpots.append([coords[0]-1, coords[1]])
	if coords[0]+1 < len(grid[coords[0]]) and grid[coords[0]+1][coords[1]] == '.':
		validSpots.append([coords[0], coords[1]+1])
	if coords[1]+1 < len(grid[coords[1]]) and grid[coords[0]][coords[1]+1] == '.':
		validSpots.append([coords[0]+1, coords[1]])
	for i in validSpots:
		grid[i[1]][i[0]] = grid[coords[1]][coords[0]] + 1
	print()
	printGrid(grid)
	return validSpots

def generateGrid(coords, fav, debug=False):
	grid = []
	for i in range(coords[0] * 2):
		line = []
		for j in range(coords[1] * 2):
			if getCoordinateStatus([j, i], fav):
				line.append('#')
			else:
				line.append('.')
		grid.append(line)
	if debug:
		printGrid(grid)
	return grid

def printGrid(grid):
	for i in grid:
		print(i)

def getCoordinateStatus(coords, fav):
	'''
	Gets the status of any given coordinate
	Returns True for wall and False for open
	'''
	assert len(coords) == 2
	assert coords[0] >= 0
	assert coords[1] >= 0

	x = coords[0]
	y = coords[1]

	n = x*x + 3*x + 2*x*y + y + y*y
	n += fav

	# Sum to binary
	b = "{0:b}".format(n)

	# Count 1s
	ones = b.count('1')

	return ones % 2 != 0

def load(path):
	with open(path, 'r') as f:
		return f
	return -1

class TestDay(unittest.TestCase):

	def test1(self):
		self.assertEqual(calc((7, 4), 10), 11)

	def test2(self):
		self.assertFalse(getCoordinateStatus((0, 0), 10))
		self.assertTrue(getCoordinateStatus((1, 0), 10))
		self.assertTrue(getCoordinateStatus((9, 6), 10))

if __name__ == '__main__':
	unittest.main()
	# Part 1:
	fav = 1358
	print(calc((31, 39), fav))
	# Part 2:

