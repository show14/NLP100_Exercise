'''
22.カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ.
'''
import json
import re

def find_article(filename):
    with open(filename, 'r') as file:
        for line in file:
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']

def extract_category_name(text):
    pattern = r'\[\[Category:(.*?)(?:\|.*)?\]\]'
    category_name = re.findall(pattern, text)
            
    return category_name

filename = 'jawiki-country.json'
text = find_article(filename)
category_text = extract_category_name(text)
print(category_text)