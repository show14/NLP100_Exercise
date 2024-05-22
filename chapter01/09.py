'''
09.Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
'''
import random

def shuffle_middle(text):
    result = []
    for word in text:    
        if len(word) <= 4:
            result.append(word)
        else:
            middle = list(word[1:-1])
            random.shuffle(middle)
            result.append(word[0] + ''.join(middle) + word[-1])
    return result

str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

text = str.split()
shuffled_text = shuffle_middle(text)
print(' '.join(shuffled_text))