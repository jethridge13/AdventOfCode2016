import unittest

def calc(coords, fav pos=[1, 1]):
	# TODO Dynamically generate grid, then Dijkstra's
	return -1

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

