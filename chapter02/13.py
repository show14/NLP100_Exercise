'''
13.col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
'''
def marge_files(col1, col2, output):
    with open(col1, 'r') as file1, open(col2, 'r') as file2, open(output, 'w') as outfile:
        # 元ファイルの1列目と2列目を結合
        for line1, line2 in zip(file1, file2):
            outfile.write(line1.strip() + '\t' + line2.strip() + '\n')

marge_files('col1.txt', 'col2.txt', 'marge.txt')
'''
ターミナルの場合
paste col1.txt col2.txt > marge.txt
'''