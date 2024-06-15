'''
18.各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''
def sort_third_column(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # 各行をタブで分割し，3コラム目の数値の逆順でソート
    sorted_lines = sorted(lines, key=lambda x: int(x.split('\t')[2]), reverse=True)
    
    # ソートされた内容を出力
    for line in sorted_lines:
        print(line.strip())
        
filename = 'popular-names.txt'
sort_third_column(filename)
'''
ターミナルの場合
sort -k3,3nr popular-names.txt
'''