'''
15.末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''
import sys

def print_last_lines(filename, n):
    """ファイルから先頭のn行だけを表示する"""
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        for line in last_n_lines:
            print(line, end='')
            
filename = "popular-names.txt"
n = int(sys.argv[1])
print_last_lines(filename, n)
'''
ターミナルの場合
tail -n N popular-names.txt
'''