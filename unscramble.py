import pickle
import vectorize

f = open('./vectors.pkl', 'rb')
dict = pickle.load(f)
f.close()

print('Word Unscrambler')
word = input('Enter a scrambled word: ')
key = vectorize.get_key(word)

if key in dict.keys():
	print(''.join(dict[key])[:-1])
else:
	print('Not found')
