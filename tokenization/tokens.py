import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')


sample_text = 'I love programming!'
tokens = word_tokenize(sample_text)

print('Tokens: ', tokens)
