import unittest
import sys

def calc(data):
	msg = ''
	for i in data:
		letter = getMostFrequentChar(i)
		msg += letter
	return msg

def calc2(data):
	msg = ''
	for i in data:
		letter = getLeastFrequentChar(i)
		msg += letter
	return msg

def getMostFrequentChar(l):
	c = ''
	counts = {}
	for i in l:
		if counts.get(i) == None:
			counts[i] = 0
		counts[i] += 1
	maxCount = 0
	for i in counts.keys():
		if counts[i] > maxCount:
			maxCount = counts[i]
			c = i
	return c

def getLeastFrequentChar(l):
	c = ''
	counts = {}
	for i in l:
		if counts.get(i) == None:
			counts[i] = 0
		counts[i] += 1
	minCount = sys.maxsize
	for i in counts.keys():
		if counts[i] < minCount:
			minCount = counts[i]
			c = i
	return c

def load(path):
	data = []
	lines = []
	with open(path, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			lines.append(line)
			assert len(line) == len(lines[-1])
	data = [list() for _ in range(len(lines[0]))]
	for i in lines:
		for j in range(len(i)):
			data[j].append(i[j])
	return data

class TestDay6(unittest.TestCase):

	def test1(self):
		data = load('Day6Test1.txt')
		self.assertEqual(calc(data), 'easter')

	def test2(self):
		t = ['a', 'a', 'b']
		self.assertEqual(getMostFrequentChar(t), 'a')

	def test3(self):
		data = load('Day6Test1.txt')
		self.assertEqual(calc2(data), 'advent')

	def test4(self):
		t = ['a', 'a', 'b']
		self.assertEqual(getLeastFrequentChar(t), 'b')

if __name__ == '__main__':
	#unittest.main()
	# Part 1: qzedlxso
	print(calc(load('Day6.txt')))
	# Part 2 ucmifjae
	print(calc2(load('Day6.txt')))
