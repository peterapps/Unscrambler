import re

def clean(s):
	return list(re.sub(r'\W+', '', s.lower()))

def can_spell(word, letters):
	word = clean(word)
	letters = clean(letters)
	for c in word:
		if c in letters:
			letters.remove(c)
		elif '?' in letters:
			letters.remove('?')
		else:
			return False
	return True

_points = [
	['?'], # 0 points
	list('aeioulnstr'), # 1 point
	list('dg'), # 2 points
	list('bcmp'), # 3 points
	list('fhvwy'), # 4 points
	['k'], # 5 points
	[], # 6 points
	[], # 7 points
	list('jx'), # 8 points
	[], # 9 points
	list('qz') # 10 points
]

points = {}
for value in range(len(_points)):
	for i in range(len(_points[value])):
		c = _points[value][i]
		points[c] = value

def score(word):
	result = 0
	word = clean(word)
	for c in word:
		result += points[c]
	return result
	
	
if __name__ == '__main__':
	letters = input('Enter your letters (put ? for blank tiles): ')

	f = open('./words.txt', 'r')
	words = [w[:-1] for w in f.readlines()]
	f.close()

	answers = []

	for word in words:
		if can_spell(word, letters): answers.append(word)
	
	answers.sort(key=score, reverse=True)
	print('\n'.join(answers))