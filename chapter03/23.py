'''
23.セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
'''
import json
import re

def find_article(filename):
    with open(filename, 'r') as file:
        for line in file:
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']

def extract_sections(text):
    pattern = r'^(={2,})\s*(.*?)\s*\1$'
    
    sections = []
    for line in text.split('\n'):
        match = re.match(pattern, line)
        if match:
            level = len(match.group(1)) - 1
            
            section_name = match.group(2)
            sections.append((section_name, level))
    return sections

filename = 'jawiki-country.json'
text = find_article(filename)
sections_text = extract_sections(text)
print(sections_text)