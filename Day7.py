import unittest
import re

def calc(data):
	count = 0
	for i in data:
		if supportsTLS(i):
			count += 1
	return count

def calc2(data):
	count = 0
	for i in data:
		if supportsSSL(i):
			count += 1
	return count

def supportsTLS(l):
	brackets = re.findall(r'\[\w+\]', l)
	strings = []
	for i in brackets:
		if searchForABBA(i):
			return False
		strings.append(l[:l.index(i)])
		l = l[l.index(i) + len(i):]
	strings.append(l)
	for i in strings:
		if searchForABBA(i):
			return True
	return False


def searchForABBA(s):
	if len(s) < 4:
		return False
	for i in range(len(s) - 3):
		if isABBA(s[i:i+4]):
			return True
	return False

def isABBA(s):
	assert len(s) == 4
	if s[0] == s[1]:
		return False
	return s[0] == s[3] and s[1] == s[2]

def supportsSSL(l):
	abas = getABAs(l)
	brackets = re.findall(r'\[\w+\]', l)
	for i in abas:
		bab = i[1] + i[0] + i[1]
		for j in brackets:
			if bab in j:
				return True
	return False

def getABAs(l):
	abas = []
	strings = []
	brackets = re.findall(r'\[\w+\]', l)
	for i in brackets:
		strings.append(l[:l.index(i)])
		l = l[l.index(i) + len(i):]
	strings.append(l)
	for i in strings:
		result = searchForABA(i)
		if result:
			abas += result
	return abas

def searchForABA(s):
	abas = []
	if len(s) < 3:
		return []
	for i in range(len(s) - 2):
		if isABA(s[i:i+3]):
			abas.append(s[i:i+3])
	return abas

def isABA(s):
	assert len(s) == 3
	return s[0] == s[2] and s[0] != s[1]

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line.replace('\n', ''))
	return data

class TestDay(unittest.TestCase):

	def test1(self):
		data = load('Day7Test1.txt')
		self.assertEqual(calc(data), 2)

	def test2(self):
		self.assertTrue(isABBA('abba'))
		self.assertFalse(isABBA('mnop'))
		self.assertFalse(isABBA('aaaa'))

	def test3(self):
		t = 'abba[mnop]qrst'
		self.assertTrue(supportsTLS(t))
		t = 'abcd[bddb]xyyx'
		self.assertFalse(supportsTLS(t))
		t = 'ioxxoj[asdfgh]zxcvbn'
		self.assertTrue(supportsTLS(t))

	def test4(self):
		t = 'ioxxoj'
		self.assertTrue(searchForABBA(t))

	def test5(self):
		data = load('Day7Test2.txt')
		self.assertEqual(calc2(data), 3)

if __name__ == '__main__':
	#unittest.main()
	# Part 1: 105
	print(calc(load('Day7.txt')))
	# Part 2: 258
	print(calc2(load('Day7.txt')))
