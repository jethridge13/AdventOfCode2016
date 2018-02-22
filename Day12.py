import unittest

def calc(data):
	reg = {}
	reg['a'] = 0
	reg['b'] = 0
	reg['c'] = 0
	reg['d'] = 0
	i = 0
	while i < len(data) - 1:
		line = parseIntoSegments(data[i])
		#print(line, reg, i)
		if line['ins'] == 'cpy':
			if type(line['x']) == int:
				reg[line['y']] = line['x']
			else:
				reg[line['y']] = reg[line['x']]
		elif line['ins'] == 'inc':
			reg[line['x']] += 1
		elif line['ins'] == 'dec':
			reg[line['x']] -= 1
		elif line['ins'] == 'jnz':
			if type(line['x']) == int:
				if line['x'] != 0:
					i += line['y'] - 1
			else:
				if reg[line['x']] != 0:
					i += line['y'] - 1
		i += 1
	return reg['a']

def parseIntoSegments(line):
	parts = line.split(' ')
	assert len(parts) >= 2
	data = {}
	data['ins'] = parts[0]
	data['x'] = atoiin(parts[1])
	if len(parts) > 2:
		data['y'] = atoiin(parts[2])
	return data

def atoiin(n):
	'''
	atoi if needed
	'''
	try:
		n = int(n)
		return n
	except:
		return n

def load(path):
	data = []
	with open(path, 'r') as f:
		for line in f:
			data.append(line.replace('\n', ''))
	return data

class TestDay(unittest.TestCase):

	def test1(self):
		data = load('Day12Test1.txt')
		self.assertEqual(calc(data), 42)

	def test2(self):
		t = 'cpy 41 a'
		d = parseIntoSegments(t)
		self.assertEqual(d['ins'], 'cpy')
		self.assertEqual(d['x'], 41)
		self.assertEqual(d['y'], 'a')

if __name__ == '__main__':
	# unittest.main()
	# Part 1: >317829
	print(calc(load('Day12.txt')))
	# Part 2:

