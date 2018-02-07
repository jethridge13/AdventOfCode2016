import unittest

def calc(data, x, y):
	'''
	data is the list of bot rules
	x is the first value to check for
	y is the second
	Returns the number of the bot that handles both x and y
	'''

	return -1

def parseLine(line):
	data = {}
	words = line.split(' ')
	data['input'] = words[0]
	if words[0] == 'value':
		data['value'] = int(words[1])
		data['bot'] = int(words[5])
		return data
	data['sendBot'] = int(words[1])
	data['low'] = int(words[6])
	data['lowType'] = words[5]
	data['high'] = int(words[11])
	data['highType'] = words[10]
	return data

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line.replace('\n', ''))
	return data

class TestDay(unittest.TestCase):

	def test1(self):
		data = load('Day10Test1.txt')
		self.assertEqual(calc(data, 5, 2), 2)

	def test2(self):
		t = 'value 5 goes to bot 2'
		parsedT = parseLine(t)
		self.assertEqual(parsedT['input'], 'value')
		self.assertEqual(parsedT['value'], 5)

		t = 'bot 2 gives low to bot 1 and high to output 0'
		parsedT = parseLine(t)
		self.assertEqual(parsedT['input'], 'bot')
		self.assertEqual(parsedT['sendBot'], 2)
		self.assertEqual(parsedT['low'], 1)
		self.assertEqual(parsedT['lowType'], 'bot')
		self.assertEqual(parsedT['high'], 0)
		self.assertEqual(parsedT['highType'], 'output')

if __name__ == '__main__':
	unittest.main()
	# Part 1: <160

	# Part 2:

