import unittest

def calc(data):
	keypad = [[1, 2, 3],
			  [4, 5, 6],
			  [7, 8, 9]]
	index = [1, 1]
	numbers = []
	for i in data:
		for j in i:
			if j == 'U':
				if index[1] > 0:
					index[1] -= 1
			elif j == 'D':
				if index[1] < len(keypad[0]) - 1:
					index[1] += 1
			elif j == 'L':
				if index[0] > 0:
					index[0] -= 1
			elif j == 'R':
				if index[0] < len(keypad) - 1:
					index[0] += 1
		numbers.append(keypad[index[1]][index[0]])
	return codify(numbers)

def calc2(data):
	keypad = [[0, 0, 1, 0, 0],
			  [0, 2, 3, 4, 0],
			  [5, 6, 7, 8, 9],
			  [0, 'A', 'B', 'C', 0],
			  [0, 0, 'D', 0, 0]]
	index = [0, 2]
	numbers = ''
	for i in data:
		for j in i:
			if j == 'U':
				if index[1] > 0 and keypad[index[1] - 1][index[0]] != 0:
					index[1] -= 1
			elif j == 'D':
				if index[1] < len(keypad[0]) - 1 and keypad[index[1] + 1][index[0]] != 0:
					index[1] += 1
			elif j == 'L':
				if index[0] > 0 and keypad[index[1]][index[0] - 1] != 0:
					index[0] -= 1
			elif j == 'R':
				if index[0] < len(keypad) - 1 and keypad[index[1]][index[0] + 1] != 0:
					index[0] += 1
		numbers += str(keypad[index[1]][index[0]])
	return numbers

def codify(l):
	assert len(l) > 0
	s = ''.join(map(str, l))
	return int(s)

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line)
	return data


class TestDay2(unittest.TestCase):

	def test1(self):
		data = load('Day2Test.txt')
		self.assertEqual(calc(data), 1985)

	def test2(self):
		data = [1, 9, 8, 5]
		self.assertEqual(codify(data), 1985)

	def test3(self):
		data = load('Day2Test.txt')
		self.assertEqual(calc2(data), '5DB3')

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 61529
	print(calc(load('Day2.txt')))
	# Part 2: C2C28
	print(calc2(load('Day2.txt')))
