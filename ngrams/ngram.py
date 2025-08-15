from nltk.tokenize import word_tokenize
from nltk.util import ngrams


sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)

unigrams = list(ngrams, 1)
print('Unigrams: ', unigrams)

bigrams = list(ngrams, 1)
print('Bigrams: ', bigrams)

trigrams = list(ngrams, 3)
print('Trigrams: ', trigrams)