'''
11.タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
def replace_tabs_with_spaces(filename):
    #ファイルを読み込む
    with open(filename, 'r') as file:
        content = file.read()
        
    #タブをスペースに置換
    replaced_content = content.replace('\t',' ')
    
    with open('output.txt', 'w') as file:
        file.write(replaced_content)
        
replace_tabs_with_spaces('popular-names.txt')
'''
ターミナルの場合
tr '\t' ' ' < popular-names.txt > output.txt
or
sed 's/\t/ /g' popular-names.txt > output.txt
or
expand -t 1 popular-names.txt > output.txt
'''