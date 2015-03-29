# coding:utf-8
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

# 日本語出力したいときの呪文
import codecs, sys
sys.stdout = codecs.getwriter('cp932')(sys.stdout)

a = u'パトカー'
b = u'タクシー'

x = ''
for i in range(1,5):
	x = x + a[i-1:i:1] + b[i-1:i:1]

print x

# print [a[i:i+4] for i in range(0,len(a),4)]
