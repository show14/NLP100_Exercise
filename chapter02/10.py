'''
10.行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
import pandas as pd

df = pd.read_table('[PATH]/popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])
print(len(df))

'''
ターミナルの場合
wc -l [PATH]/popular-names.txt
'''