import unittest

def calc(data):
	coords = [0, 0]
	direction = 'N'
	dirR = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
	dirL = {v: k for k, v in dirR.items()}
	for i in data:
		newDir, n = getParts(i)
		if newDir == 'R':
			direction = dirR[direction]
		else:
			direction = dirL[direction]
		if direction == 'S' or direction == 'W':
			n *= -1
		if direction == 'N' or direction == 'S':
			coords[0] += n
		else:
			coords[1] += n
	return score(coords)

def calc2(data):
	coords = [0, 0]
	direction = 'N'
	dirR = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
	dirL = {v: k for k, v in dirR.items()}
	visited = {}
	for i in data:
		newDir, n = getParts(i)
		if newDir == 'R':
			direction = dirR[direction]
		else:
			direction = dirL[direction]
		if direction == 'S' or direction == 'W':
			n *= -1
		if direction == 'N' or direction == 'S':
			for i in range(abs(n)):
				if n >= 0:
					coords[0] += 1
				else:
					coords[0] -= 1
				if visited.get(tuple(coords)):
					return score(coords)
				visited[tuple(coords)] = 1
		else:
			for i in range(abs(n)):
				if n >= 0:
					coords[1] += 1
				else:
					coords[1] -= 1
				if visited.get(tuple(coords)):
					return score(coords)
				visited[tuple(coords)] = 1

def score(tup):
	return abs(tup[0]) + abs(tup[1])

def getParts(tup):
	return tup[0], int(tup[1:])

def load(path):
	data = []
	with open(path, 'r') as f:
		data = f.read().split(', ')
	return data

class TestDay1(unittest.TestCase):

	def test1(self):
		data = ['R2', 'L3']
		self.assertEqual(calc(data), 5)
		data = ['R2', 'R2', 'R2']
		self.assertEqual(calc(data), 2)
		data = ['R5', 'L5', 'R5', 'R3']
		self.assertEqual(calc(data), 12)

	def test2(self):
		coords = [-2, 5]
		self.assertEqual(score(coords), 7)

	def test3(self):
		t = getParts('R2')
		self.assertEqual(t[0], 'R')
		self.assertEqual(t[1], 2)

	def test4(self):
		data = ['R8', 'R4', 'R4', 'R8']
		self.assertEqual(calc2(data), 4)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 239
	print(calc(load('Day1.txt')))
	# Part 2: 141
	print(calc2(load('Day1.txt')))
