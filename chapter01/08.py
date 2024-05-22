'''
08.暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
英小文字ならば(219 - 文字コード)の文字に置換 その他の文字はそのまま出力 この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''
def cipher(str):
    result = []
    for char in str:
        if char.islower():
            result.append(chr(219 - ord(char)))
        else:
            result.append(char)
    return ''.join(result)

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

encrypted = cipher(str)
decrypted = cipher(encrypted)

print("Original:", str)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)