# coding:utf-8
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

# 日本語出力したいときの呪文
import codecs, sys
sys.stdout = codecs.getwriter('cp932')(sys.stdout)

a = u'パタトクカシーー'
x = a[0:6:2]
print x