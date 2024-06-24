'''
21.カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''
import json

def find_article(filename):
    with open(filename, 'r') as file:
        for line in file:
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']

def extract_categories(text):
    categories = []
    
    for line in text.split('\n'):
        if "[[Category:" in line:
            categories.append(line)
    return categories

filename = 'jawiki-country.json'
text = find_article(filename)
extract_text = extract_categories(text)
print(extract_text)