# coding:utf-8
# ↑これ書いておかないと「SyntaxError: Non-ASCII character」

# []は先頭から１，２の引数が何文字目かを意味して、３つめがどういうルールで文字を取得するか、みたい

# これは当然OK
a = 'stressed'
print a[::-1]

# これはダメ参照的な変更じゃない
a = 'stressed'
a[::-1]
print a
