'''
06.集合
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''
def ngram(n, lst):
    return (lst[i:i+n] for i in range(len(lst) - n + 1))

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(2, tuple(str1)))
Y = set(ngram(2, tuple(str2)))
union = X | Y
intersection = X & Y
difference = X - Y

#"se"というbi-gramがXおよびYに含まれるか
se_in_X = ("s","e") in X
se_in_Y = ("s","e") in Y

print("X:",X)
print("Y:",Y)
print("和集合:",union)
print("積集合:",intersection)
print("差集合:",difference)
print("'se'がXに含まれるか:", se_in_X)
print("'se'がYに含まれるか:", se_in_Y)