'''
05.n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''

def ngram(n, lst):
  return list(lst[i:i+n] for i in range(len(lst) - n + 1))

str = "I am an NLPer"
words = str.split()
word_bigrams = ngram(2, words)

characters = list(str)
char_bigrams = ngram(2, characters)

print("単語bi-gram:", word_bigrams)
print("文字bi-gram:", char_bigrams)