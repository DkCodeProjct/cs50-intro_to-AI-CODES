import nltk
nltk.download('punkt')

import math
import os
from collections import Counter
sentence = 'i love doing cs50AI.'
print(f'EX. Senetence:{sentence}')
n0 = 1

unigrams = nltk.ngrams(sentence.split(), n0)
print("Unigrams::")
for gram in unigrams:
    print(f'    -{gram}')


bigrams = nltk.bigrams(sentence.split())
print("\nBigrams::")
for gram in bigrams:
    print(f'    -{gram}')


trigrams = nltk.trigrams(sentence.split())
print('\nTrigrams::')
for gram in trigrams:
     print(f'    -{gram}')


def main():
    useGram = int(input('To n-grams in lacan/txt Choose: Gram[1/2/3]: '))
    if useGram > 3:
        print('>3')
    corpus = loadData('lacan.txt')


    ngrams = Counter(nltk.ngrams(corpus, useGram))

    for nGram, freq in ngrams.most_common(10):
        print(f'\n{ngrams}: {freq}')


def loadData(dir):
    contents = []
  
    with open(dir, 'r') as f:
        contents.extend([
            word.lower() for word in 
            nltk.word_tokenize(f.read())
            if any(c.isalpha() for c in word)
        ])
    
    return contents


if __name__ == '__main__':
    main()

