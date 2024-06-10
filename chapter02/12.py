'''
12.1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
'''
def extract_columns(filename):
    col1 = []
    col2 = []
    
    #ファイルを読み来む
    with open(filename, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 2:
                col1.append(columns[0])
                col2.append(columns[1])
    
    with open('col1.txt', 'w') as f1:
        for item in col1:
            f1.write(item + '\n')
            
    with open('col2.txt', 'w') as f2:
        for item in col2:
            f2.write(item + '\n')
            
extract_columns('popular-names.txt')
'''
ターミナルの場合
cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt
'''