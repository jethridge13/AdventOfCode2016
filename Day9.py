import unittest

def calc(line):
	decompressed = ''
	lines = breakIntoSegments(line)
	for i in lines:
		decompressed += decompress(i)
	return len(decompressed)

def calc2(line):
	# TODO
	s = 0
	lines = breakIntoSegments(line)
	for i in lines:
		if ')' not in i:
			s += len(i)
		elif i.find(')') == i.rfind(')'):
			index = i.find('(')
			endIndex = i.find(')')
			marker = i[index:endIndex+1]
			length, repeat = getNumbersFromMarker(marker)
			s += length * repeat
			s += len(i[:index])
		else:
			nested = i
			while nested.find(')') != nested.rfind(')'):
				index = nested.find('(')
				s += len(nested[:index])
				endIndex = nested.find(')')
				marker = nested[index:endIndex+1]
				_, repeat = getNumbersFromMarker(marker)
				nested = nested[endIndex+1:]
				secondIndex = nested.find('(')
				secondEndIndex = nested.find(')')
				secondMarker = nested[secondIndex:secondEndIndex+1]
				_, secondRepeat = getNumbersFromMarker(secondMarker)
				newRepeat = str(repeat * secondRepeat)
				nested = nested[:nested.find('x') + 1] + newRepeat + nested[endIndex-1:]
			index = nested.find('(')
			endIndex = nested.find(')')
			marker = nested[index:endIndex+1]
			length, repeat = getNumbersFromMarker(marker)
			s += length * repeat
	return s

def decompress(s):
	if '(' not in s:
		return s

	result = ''
	index = s.find('(')
	endIndex = s.find(')')
	result += s[:index]
	marker = s[index:endIndex+1]
	length, repeat = getNumbersFromMarker(marker)
	segment = s[endIndex+1:endIndex+1+length]
	for i in range(repeat):
		result += segment
	if len(segment) + endIndex + 1 < len(s):
		result += s[len(segment) + endIndex + 1:]
	return result

def getNumbersFromMarker(t):
	a = int(t[t.find('(')+1:t.find('x')])
	b = int(t[t.find('x')+1:t.find(')')])
	return a, b

def breakIntoSegments(s):
	segments = []
	while '(' in s:
		index = s.find('(')
		endIndex = s.find(')')
		marker = s[index:endIndex+1]
		length, _ = getNumbersFromMarker(marker)
		segmentEnd = endIndex + 1 + length
		segments.append(s[:segmentEnd])
		s = s[segmentEnd:]
	if s:
		segments.append(s)
	return segments

def load(path):
	data = ''
	with open(path, 'r') as f:
		data = f.readline()
	return data

class TestDay9(unittest.TestCase):

	def test1(self):
		t = 'ADVENT'
		self.assertEqual(calc(t), 6)
		t = 'A(1x5)BC'
		self.assertEqual(calc(t), 7)
		t = '(3x3)XYZ'
		self.assertEqual(calc(t), 9)
		t = 'A(2x2)BCD(2x2)EFG'
		self.assertEqual(calc(t), 11)
		t = '(6x1)(1x3)A'
		self.assertEqual(calc(t), 6)
		t = 'X(8x2)(3x3)ABCY'
		self.assertEqual(calc(t), 18)

	def test2(self):
		t = 'ADVENT'
		self.assertEqual(decompress(t), 'ADVENT')
		t = 'A(1x5)BC'
		self.assertEqual(decompress(t), 'ABBBBBC')
		t = '(3x3)XYZ'
		self.assertEqual(decompress(t), 'XYZXYZXYZ')
		t = '(6x1)(1x3)A'
		self.assertEqual(decompress(t), '(1x3)A')
		t = 'X(8x2)(3x3)ABCY'
		self.assertEqual(decompress(t), 'X(3x3)ABC(3x3)ABCY')

	def test3(self):
		t = '(1x3)'
		a, b = getNumbersFromMarker(t)
		self.assertEqual(a, 1)
		self.assertEqual(b, 3)
		t = '(3x3)'
		a, b = getNumbersFromMarker(t)
		self.assertEqual(a, 3)
		self.assertEqual(b, 3)

	def test4(self):
		t = 'A(2x2)BCD(2x2)EFG'
		r = breakIntoSegments(t)
		self.assertEqual(len(r), 3)

	def test5(self):
		t = 'ADVENT'
		self.assertEqual(calc2(t), 6)
		t = 'A(1x5)BC'
		self.assertEqual(calc(t), 7)
		t = '(3x3)XYZ'
		self.assertEqual(calc(t), 9)
		t = 'X(8x2)(3x3)ABCY'
		self.assertEqual(calc2(t), 20)
		t = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
		self.assertEqual(calc2(t), 241920)
		t = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
		self.assertEqual(calc2(t), 445)


if __name__ == '__main__':
	unittest.main()
	# Part 1: 97714
	print(calc(load('Day9.txt')))
	# Part 2:
	print(calc2(load('Day9.txt')))
