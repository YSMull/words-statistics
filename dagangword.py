#coding=gbk
import simplify_word as sw
import re

dagang = open('data/5495大纲词汇.txt')
dagangwords = []
for eachLine in dagang:
    dagangwords.append(sw.simplify_word(re.split("[^A-Za-z]", eachLine)[0].lower()))
    #print re.split("[^A-Za-z]", eachLine)[0]
print len(list(set(dagangwords)))
dagangwords = list(set(dagangwords))
