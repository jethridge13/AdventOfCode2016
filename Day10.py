import unittest

def calc(data, x, y):
	'''
	data is the list of bot rules
	x is the first value to check for
	y is the second
	Returns the number of the bot that handles both x and y
	'''
	bots = generateBots(data)
	output = {}

	# TODO Now that all the bots are set up, run through
	botsToSend = []
	for i in bots.keys():
		botsToCheck = []
		if not bots[i].get('values'):
			bots[i]['values'] = []
		if len(bots[i]['values']) == 2:
			# If bot is holding 2 values, check if those are the values
			# for which we are searching
			if x in bots[i]['values'] and y in bots[i]['values']:
				return i
			# Otherwise, distribute accordingly and then check
			bots[i]['high'] = max(bots[i]['values'])
			bots[i]['low'] = min(bots[i]['values'])
			bots[i]['values'] = []
			if bots[i]['rules']['highType'] == 'bot':
				if not bots[bots[i]['rules']['high']].get('values'):
					bots[bots[i]['rules']['high']]['values'] = []
				bots[bots[i]['rules']['high']]['values'].append(bots[i]['high'])
				botsToCheck.append(bots[i]['high'])
			else:
				output[bots[i]['rules']['high']].append(bots[i]['high'])
			if bots[i]['rules']['lowType'] == 'bot':
				if not bots[bots[i]['rules']['low']].get('values'):
					bots[bots[i]['rules']['low']]['values'] = []
				bots[bots[i]['rules']['low']]['values'].append(bots[i]['low'])
				botsToCheck.append(bots[i]['low'])
			else:
				output[bots[i]['rules']['low']].append(bots[i]['low'])
			del bots[i]['high']
			del bots[i]['low']


			while botsToCheck:
				if not bots[botsToCheck[0]].get('values'):
					bots[botsToCheck[0]]['values'] = []
				if len(bots[botsToCheck[0]]['values']) == 2:
					bot = bots[botsToCheck[0]]
					if x in bot['values'] and y in bot['values']:
						return botsToCheck[0]
					bot['high'] = max(bot['values'])
					bot['low'] = min(bot['values'])
					bot['values'] = []
					if bot['rules']['highType'] == 'bot':
						bots[bot['rules']['high']]['values'].append(bot['high'])
						botsToCheck.append(bot['high'])
					else:
						output[bot['rules']['high']].append(bot['high'])
					if bot['rules']['lowType'] == 'bot':
						bots[bot['rules']['low']]['values'].append(bot['low'])
						botsToCheck.append(bots[i]['low'])
					else:
						output[bot['rules']['low']].append(bot['low'])
					del bot['high']
					del bot['low']
				botsToCheck = botsToCheck[1:]
			for i in bots.keys():
				print(i, bots[i])
	return -1

def parseLine(line):
	data = {}
	words = line.split(' ')
	data['input'] = words[0]
	if words[0] == 'value':
		data['value'] = int(words[1])
		data['bot'] = int(words[5])
		return data
	data['bot'] = int(words[1])
	data['low'] = int(words[6])
	data['lowType'] = words[5]
	data['high'] = int(words[11])
	data['highType'] = words[10]
	return data

def generateBots(data):
	bots = {}
	for i in data:
		rules = parseLine(i)
		if rules['input'] == 'value':
			# If bot takes input from input
			bot = bots.get(rules['bot'], {})
			# Add value to bots list of values
			if not bot.get('values'):
				bot['values'] = []
			bot['values'].append(rules['value'])
			bots[rules['bot']] = bot
		elif rules['input'] == 'bot':
			# If bot takes input from bot
			sendBot = bots.get(rules['bot'], {})
			botRules = {}
			botRules['highType'] = rules['highType']
			botRules['lowType'] = rules['lowType']
			botRules['high'] = rules['high']
			botRules['low'] = rules['low']
			sendBot['rules'] = botRules
			bots[rules['bot']] = sendBot
	return bots

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
		self.assertEqual(parsedT['bot'], 2)
		self.assertEqual(parsedT['low'], 1)
		self.assertEqual(parsedT['lowType'], 'bot')
		self.assertEqual(parsedT['high'], 0)
		self.assertEqual(parsedT['highType'], 'output')

if __name__ == '__main__':
	#unittest.main()
	# Part 1: <106
	print(calc(load('Day10.txt'), 61, 17))
	# Part 2:

