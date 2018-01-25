import unittest
import re

def calc(data):
	count = 0
	for i in data:
		if validateTriangle(i):
			count += 1
	return count

def validateTriangle(sides):
	assert len(sides) == 3
	a = sides[0]
	b = sides[1]
	c = sides[2]
	if a + b <= c or a + c <= b or b + c <= a:
		return False
	return True

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			l = line.replace('\n', '')
			l = re.sub(r'\s+', ' ', l)
			l = l.split()
			sides = []
			for i in l:
				sides.append(int(i))
			data.append(sides)
	return data

def load2(path):
	data = []
	setOfThree = []
	with open(path, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			line = re.sub(r'\s+', ' ', line)
			line = line.split()
			if len(setOfThree) < 3:
				setOfThree.append(line)
			if len(setOfThree) == 3:
				for i in range(3):
					tmp = []
					for j in setOfThree:
						tmp.append(int(j[i]))
					data.append(tmp)
				setOfThree = []
	return data

class TestDay3(unittest.TestCase):

	def test1(self):
		data = load('Day3.txt')
		self.assertEqual(data[0], [883, 357, 185])

	def test2(self):
		data = [5, 10, 25]
		self.assertFalse(validateTriangle(data))

	def test3(self):
		data = load2('Day3.txt')
		self.assertEqual(data[0], [883, 572, 842])

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 982
	print(calc(load('Day3.txt')))
	# Part 2: 1826
	print(calc(load2('Day3.txt')))
