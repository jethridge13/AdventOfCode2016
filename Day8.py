import unittest

def calc(data):
	l = [['.' for x in range(50)] for y in range(6)]
	for i in data:
		line = parseLine(i)
		if line['op'] == 'rect':
			l = rect(line['a'], line['b'], l)
		elif line['op'] == 'column':
			l = rotateColumn(line['x'], line['n'], l)
		elif line['op'] == 'row':
			l = rotateRow(line['y'], line['n'], l)
	for i in l:
		print(i)
	return score(l)

def score(l):
	s = 0
	for i in l:
		for j in i:
			if j == '#':
				s += 1
	return s

def rect(a, b, l):
	assert type(l) == list
	for i in range(a):
		for j in range(b):
			l[j][i] = '#'
	return l

def rotateColumn(x, n, l):
	assert type(l) == list
	for i in range(n):
		lastIndex = ''
		for j in range(len(l)):
			if lastIndex:
				lastIndex, l[j][x] = l[j][x], lastIndex
			else:
				lastIndex = l[j][x]
				l[j][x] = l[j-1][x]
		lastIndex = ''
	return l

def rotateRow(y, n, l):
	assert type(l) == list
	for i in range(n):
		lastIndex = ''
		for j in range(len(l[y])):
			if lastIndex:
				lastIndex, l[y][j] = l[y][j], lastIndex
			else:
				lastIndex = l[y][j]
				l[y][j] = l[y][j-1]
		lastIndex = ''
	return l

def parseLine(l):
	data = {}
	l = l.split(' ')
	if l[0] == 'rect':
		data['op'] = 'rect'

		a = int(l[1][:l[1].index('x')])
		b = int(l[1][l[1].index('x') + 1:])
		data['a'] = a
		data['b'] = b
		return data
	if l[0] == 'rotate':
		assert l[1] == 'row' or l[1] == 'column'
		if l[1] == 'column':
			data['op'] = 'column'
			data['x'] = int(l[2][l[2].index('=')+1:])
			data['n'] = int(l[4])
			return data
		else:
			data['op'] = 'row'
			data['y'] = int(l[2][l[2].index('=')+1:])
			data['n'] = int(l[4])
			return data
	return data

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line.replace('\n', ''))
	return data

class TestDay8(unittest.TestCase):

	def test1(self):
		data = load('Day8Test1.txt')
		self.assertEqual(calc(data), 6)

	def test2(self):
		t = [['.' for x in range(7)] for y in range(3)]
		a = [['#', '#', '#', '.', '.', '.', '.'],
			 ['#', '#', '#', '.', '.', '.', '.'],
			 ['.', '.', '.', '.', '.', '.', '.']]
		self.assertEqual(rect(3, 2, t), a)

	def test3(self):
		t = [['#', '#', '#', '.', '.', '.', '.'],
			 ['#', '#', '#', '.', '.', '.', '.'],
			 ['.', '.', '.', '.', '.', '.', '.']]
		a = [['#', '.', '#', '.', '.', '.', '.'],
			 ['#', '#', '#', '.', '.', '.', '.'],
			 ['.', '#', '.', '.', '.', '.', '.']]
		self.assertEqual(rotateColumn(1, 1, t), a)

	def test4(self):
		t = [['#', '.', '#', '.', '.', '.', '.'],
			 ['#', '#', '#', '.', '.', '.', '.'],
			 ['.', '#', '.', '.', '.', '.', '.']]
		a = [['.', '.', '.', '.', '#', '.', '#'],
			 ['#', '#', '#', '.', '.', '.', '.'],
			 ['.', '#', '.', '.', '.', '.', '.']]
		self.assertEqual(rotateRow(0, 4, t), a)

	def test5(self):
		t = 'rect 3x2'
		t = parseLine(t)
		self.assertEqual(t['op'], 'rect')
		self.assertEqual(t['a'], 3)
		self.assertEqual(t['b'], 2)

		t = 'rotate column x=1 by 1'
		t = parseLine(t)
		self.assertEqual(t['op'], 'column')
		self.assertEqual(t['x'], 1)
		self.assertEqual(t['n'], 1)

		t = 'rotate row y=0 by 4'
		t = parseLine(t)
		self.assertEqual(t['op'], 'row')
		self.assertEqual(t['y'], 0)
		self.assertEqual(t['n'], 4)

	def test6(self):
		t = [['#', '#', '#', '.', '.', '.', '.'],
			 ['#', '#', '#', '.', '.', '.', '.'],
			 ['.', '.', '.', '.', '.', '.', '.']]
		self.assertEqual(score(t), 6)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 110
	print(calc(load('Day8.txt')))
	# Part 2: ZJHRKCPLYJ
