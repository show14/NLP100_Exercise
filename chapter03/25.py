'''
25.テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''
import json
import re

def remove_markup(text):
    markup_pattern = r"('{2,5})(.*?)(\1)"
    text = re.sub(markup_pattern, r'\2', text)
    return text

def find_article(filename):
    with open(filename, 'r') as file:
        for line in file:
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']

def extract_infobox(text):
    pattern = r'^\{\{基礎情報[^|]*\n(.*?)^\}\}'
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not match:
        return None
    
    infobox_content = match.group(1)

    dict = {}
    pattern_fields = r'\|([^=]+?)\s*=\s*(.*?)(?=\n\||\n\})'
    for field, value in re.findall(pattern_fields, infobox_content, re.DOTALL):
        cleaned_value = remove_markup(value)
        dict[field.strip()] = cleaned_value.strip()
        
    return dict

filename = 'jawiki-country.json'
text = find_article(filename)
infobox = extract_infobox(text)
if infobox:
    for key, value in infobox.items():
        print(f"{key}: {value}")