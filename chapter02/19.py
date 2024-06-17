'''
19.各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
'''
from collections import Counter

def count_name(filename):
    counter = Counter()
    
    with open(filename, 'r') as file:
        for line in file:
            name = line.split('\t')[0]
            counter[name] += 1
        
    # 頻度が高い順にソート
    for name, count in counter.most_common():
        print(count, name)

filename = 'popular-names.txt'
count_name(filename)
'''
ターミナルの場合
cut -f1 popular-names.txt | sort | uniq -c | sort -nr
'''