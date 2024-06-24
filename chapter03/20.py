'''
20.JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''
import json 

def find_article(filename):
    with open(filename, 'r') as file:
        for line in file:
            article = json.load(line)
            if article['title'] == 'イギリス':
                return article['text']

filename = 'jawiki-country.json'
text = find_article(filename)
print(text)