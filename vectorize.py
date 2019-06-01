import pickle

def get_key(word):
	# Vectorize word
	letters = list('abcdefghijklmnopqrstuvwxyz')
	word = list(word.lower())
	vect = [0] * len(letters)
	for c in word:
		if c in letters: vect[letters.index(c)] += 1
	
	# Create key from vector
	return "-".join([str(n) for n in vect])

if __name__ == '__main__':
	f = open('./words.txt', 'r')
	words = f.readlines()
	f.close()
	num_words = len(words)
	print('Vectorizing {} words'.format(num_words))

	perc = 0

	vectors = {}

	for i in range(num_words):
		# Display progress
		current_perc = int(i / num_words * 10)
		if int(current_perc) > perc:
			perc = current_perc
			print('{}%'.format(perc*10))
		
		key = get_key(words[i])
		if key in vectors:
			vectors[key].append(words[i])
		else:
			vectors[key] = [words[i]]

	print('Saving vectors')
	f = open('vectors.pkl', 'wb')
	pickle.dump(vectors, f)
	f.close()
	print('Done')
