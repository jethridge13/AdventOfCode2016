import unittest
import hashlib

def calc(doorID):
	password = ''
	index = 0
	while len(password) < 8:
		h = getHash(doorID + str(index))
		if startsWithFiveZeros(h):
			password += h[5]
		index += 1
	return password

def calc2(doorID):
	password = [None] * 8
	index = 0
	filledSlots = 0
	while filledSlots < 8:
		h = getHash(doorID + str(index))
		if startsWithFiveZeros(h):
			i = h[5]
			if i.isdigit():
				i = int(i)
			else:
				index += 1
				continue
			if i > 7:
				index += 1
				continue
			if password[i] == None:
				password[i] = h[6]
				filledSlots += 1
		index += 1
	return ''.join(password)

def startsWithFiveZeros(h):
	return h.startswith('00000')

def getHash(s):
	h = hashlib.md5()
	h.update(s.encode())
	return h.hexdigest()


class TestDay5(unittest.TestCase):
	
	def test1(self):
		s = 'abc'
		self.assertEqual(calc(s), '18f47a30')
	
	def test2(self):
		s = 'abc5017308'
		self.assertTrue(str(getHash(s)).startswith('000008f82'))

	def test3(self):
		s = 'abc5017308'
		s = getHash(s)
		self.assertTrue(startsWithFiveZeros(s))

	def test4(self):
		s = 'abc'
		self.assertEqual(calc2(s), '05ace8e3')


if __name__ == '__main__':
	inp = 'ffykfhsq'
	#unittest.main()
	# Part 1: c6697b55
	print(calc(inp))
	# Part 2: 8c35d1ab
	print(calc2(inp))
