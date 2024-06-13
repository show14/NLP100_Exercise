'''
16.ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
'''
import sys

def split_file(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 各分割の行数を計算する
    total_lines = len(lines)
      # 切り上げ除算
    size = (total_lines + n - 1) // n

    # ファイルを分割して保存
    for i in range(n):
        with open(f"split_file_{i}", 'w') as file:
            s_index = i * size
            e_index = s_index + size
            file.writelines(lines[s_index:e_index])

filename = "popular-names.txt"
n = int(sys.argv[1])
split_file(filename, n)
'''
ターミナルの場合
split -d -l $(($(wc -l < popular-names.txt) / 10 + 1)) popular-names.txt split_file_
'''