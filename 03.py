# coding:utf-8
# 日本語出力したいときの呪文
import codecs, sys
sys.stdout = codecs.getwriter('cp932')(sys.stdout)
import string

# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．


row_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
replace_str = row_str.translate(string.maketrans("", ""), ",.")
split_srt = replace_str.split(" ")

x = list()
for i in split_srt:
	x.append(len(i))

print x

