import pandas as pd

df = pd.read_table('./github/nlp100/chapter02/data/popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])
print(len(df))

'''
ターミナルの場合
wc -l ./github/nlp100/chapter02/data/popular-names.txt
'''