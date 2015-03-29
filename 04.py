# coding:utf-8
# 日本語出力したいときの呪文
import codecs, sys
sys.stdout = codecs.getwriter('cp932')(sys.stdout)
import string

# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．


row_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
replace_str = row_str.translate(string.maketrans("", ""), ",.")
str_list = replace_str.split(" ")


# list作成
x = [1, 5, 6, 7, 8, 9, 15, 16, 19]
y = dict()
n = 1
for str_snippet in str_list:
	if n in x:
		y[n] = str_snippet[0:1:1]
	else:
		y[n] = str_snippet[0:2:1]
	n += 1

print y
