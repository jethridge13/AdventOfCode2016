import unittest

def calc(data):
	validRooms = getValidRooms(data)
	IDSum = 0
	for i in validRooms:
		IDSum += data[i]['sectorID']
	return IDSum

def calc2(data):
	validRooms = getValidRooms(data)
	for i in validRooms:
		name = unencryptName(data[i])
		if 'north' in name:
			data[i]['realName'] = name
			return data[i]

def getValidRooms(data):
	validRooms = []
	for i in data.keys():
		if genChecksum(data[i]['name']) == data[i]['checksum']:
			validRooms.append(i)
	return validRooms

def genChecksum(name):
	charMap = {}
	for i in name:
		if i == '-':
			continue
		if not charMap.get(i):
			charMap[i] = 1
		else:
			charMap[i] += 1
	checksum = ''
	while len(charMap.keys()) > 0:
		maxKey = []
		maxValue = 0
		for key in charMap:
			if charMap[key] > maxValue:
				maxKey = [key]
				maxValue = charMap[key]
			elif charMap[key] == maxValue:
				maxKey.append(key)
		if len(maxKey) == 1:
			checksum += str(maxKey[0])
			if len(checksum) == 5:
				return checksum
			del charMap[maxKey[0]]
		else:
			maxKey = sorted(maxKey)
			for i in maxKey:
				checksum += i
				if len(checksum) == 5:
					return checksum
				del charMap[i]
	return checksum

def unencryptName(line):
	shift = line['sectorID']
	name = ''
	for i in line['name']:
		if i == '-':
			name += ' '
		else:
			n = ord(i)
			n += (shift % 26)
			# 122 = 'z'
			if n > 122:
				# 97 = 'a'
				# If ascii code is greater than 'z',
				# Wrap aroud back to 'a'
				n = (n - 123) + 97
			name += chr(n)
	return name

def load(path):
	data = {}
	with open(path, 'r') as f:
		for line in f:
			line = line.replace('\n', '')
			data[line] = parseLine(line)
	return data

def parseLine(line):
	lineMap = {}
	lineMap['name'] = line[:line.rindex('-')]
	lineMap['sectorID'] = int(line[line.rindex('-')+1:line.index('[')])
	lineMap['checksum'] = line[line.index('[')+1:line.index(']')]
	return lineMap

class TestDay(unittest.TestCase):

	def test1(self):
		data = load('Day4.txt')
		self.assertEqual(data['aczupnetwp-dnlgpyrpc-sfye-dstaatyr-561[patyc]']['name'], 'aczupnetwp-dnlgpyrpc-sfye-dstaatyr')
		self.assertEqual(data['aczupnetwp-dnlgpyrpc-sfye-dstaatyr-561[patyc]']['sectorID'], 561)
		self.assertEqual(data['aczupnetwp-dnlgpyrpc-sfye-dstaatyr-561[patyc]']['checksum'], 'patyc')

	def test2(self):
		checksum = genChecksum('aaaaa-bbb-z-y-x')
		self.assertEqual(checksum, 'abxyz')

	def test3(self):
		t = calc(load('Day4Test1.txt'))
		self.assertEqual(t, 1514)

	def test4(self):
		data = {}
		data['name'] = 'qzmt-zixmtkozy-ivhz'
		data['sectorID'] = 343
		data['checksum'] = 'zimth'
		self.assertEqual(unencryptName(data), 'very encrypted name')


if __name__ == '__main__':
	#unittest.main()
	# Part 1: 278221
	print(calc(load('Day4.txt')))
	# Part 2: 267
	print(calc2(load('Day4.txt')))
