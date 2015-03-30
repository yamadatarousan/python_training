# coding:utf-8
# 日本語出力したいときの呪文
import codecs, sys
sys.stdout = codecs.getwriter('cp932')(sys.stdout)
import string