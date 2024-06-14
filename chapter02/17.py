'''
17.１列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
'''
def unique_column(filename):
    unique_names = set()
    
    with open(filename, 'r') as file:
        for item in file:
            for line in file:
                name = line.strip().split('\t')[0]
                unique_names.add(name)
                sorted_names = sorted(unique_names)
    return sorted_names

filename = 'popular-names.txt'
unique_first_column = unique_column(filename)
print(unique_first_column)
'''
ターミナルの場合
cut -f1 -d$'\t' popular-names.txt | sort | uniq
'''