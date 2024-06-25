'''
24.ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''
import json
import re

def find_article(filename):
    with open(filename, 'r') as file:
        for line in file:
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']

def extract_file(text):
    pattern = r'\[\[(File:|ファイル:)(.*?)\|'
    files = re.findall(pattern, text)
            
    return [file_name[1] for file_name in files]

filename = 'jawiki-country.json'
text = find_article(filename)
files = extract_file(text)
for file in files:
    print(file)