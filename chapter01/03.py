'''
03.円周率
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(",", "").replace(".", "")  # ,と.を除去
splits = str.split()  # スペースで区切って単語ごとのリストを作成
ans = [len(i) for i in splits]

print(ans)

