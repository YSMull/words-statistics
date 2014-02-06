#coding=gbk
import simplify_word as sw
import re

bw = open('data/basic_words.txt')
basicwords = []
for eachLine in bw:
    basicwords.append(sw.simplify_word(re.split("[^A-Za-z]", eachLine)[0].lower()))
    #print re.split("[^A-Za-z]", eachLine)[0]
print len(list(set(basicwords)))
basicwords = list(set(basicwords))
