'''
14.先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''
import sys

def print_initial_lines(filename, n):
    """ファイルから先頭のn行だけを表示する"""
    
    with open(filename, 'r') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line, end='')
            
filename = "popular-names.txt"
n = int(sys.argv[1])
print_initial_lines(filename, n)
'''
ターミナルの場合
head -n N popular-names.txt
'''