#coding=gbk
from __future__ import division
import re
import matplotlib.pyplot as plt
import numpy as np
import en


otherwordlist = []
def simplify_word(a):
    #如果已经可以判断是名词,动词,形容词,副词,连词
    if en.is_noun(a) or en.is_verb(a) or en.is_adjective(a) or en.is_adverb(a) or en.is_connective(a):
        return a
    try:#测试是否为动词,如果是则返回
        en.is_verb(en.verb.present(a))
        return en.verb.present(a)
    except:#否则继续检查
        pass
    
    #测试是否是名词
    if en.is_noun(en.noun.singular(a)):
        return en.noun.singular(a)
    otherwordlist.append(a)
    #print a
    return a
    
#print simplify_word('dishonoring')

    

dagang = open('5495大纲词汇.txt')

dagangwords = []
for eachLine in dagang:
    dagangwords.append(simplify_word(re.split("[^A-Za-z]", eachLine)[0].lower()))
    #print re.split("[^A-Za-z]", eachLine)[0]
#print len(list(set(dagangwords)))
dagangwords = list(set(dagangwords))
#print 'been' in dagangwords
llen = []
nxx = range(33)#sum of different words in every exam
for i in range(33):
    filename = "%d.txt" % i
    #print i
    #print filename

    x = open(filename)
    wordsLists = []
    for eachLine in x:
        wordsLists += [simplify_word(word.lower()) for word in re.split("[^A-Za-z]", eachLine) if word != "" and word[-1].islower()]
    x.close()
    #print len(wordsLists)
    wordsum = {}
    for eachWord in wordsLists:
        wordsum[eachWord] = 0
    for eachWord in wordsLists:
        wordsum[eachWord] += 1
    xx = sorted(wordsum.iteritems(), key = lambda e:e[1], reverse = True)
    '''to ensure that the word appear at the head of a sentence 
    will not be treated differently, so first we turn each word to 
    lower state and second we use list(set()) multiple methed which
    will eliminate iterative word ,to achieve that aim'''
    nxx[i] = list(set([ii[0] for ii in xx]))
    llen.append(len(nxx[i]))
    
    #print xx
#print llen
#print nxx[0]
s = []
lw = range(32)
for i in range(32):
    lw[i] = 0
for i in range(32):
    s += nxx[i]
    for j in nxx[i+1]:
        if j not in s:
            lw[i] += 1

lw = [llen[0]] + lw
#print lw

sset = range(33)
s = set(nxx[0])
for i in range(33):
    s &= set(nxx[i])

#print 's = ' ,s

es = range(32)
esr1 = range(32)
esr2 = range(32)
esr3 = range(32)
for i in range(32):
    es[i] = len(set(nxx[i]) & set(nxx[i+1]))
    esr1[i] = es[i] * 2 / (llen[i] + llen[i+1])
    esr2[i] = es[i] / llen[i+1]
    esr3[i] = es[i] / llen[i]
    #print '%d,%d' %(2*es[i], (llen[i] + llen[i+1]))
    #print esr[i]
#print es
#print esr1
#print esr2
#plt.plot(1980*np.ones(32)+range(32), esr1, 'r-o')
#plt.plot(1980*np.ones(32)+range(32), esr2, 'b-o')
#plt.plot(1980*np.ones(32)+range(32), esr3, 'y-o')

indagang = np.zeros(33)
chaogangword = {}
for j in range(33):
    if 'been' in nxx[j]:
        print j,'hehe'
    for k in nxx[j]:
        if k not in dagangwords:
            indagang[j] += 1
            if chaogangword.has_key(k):
                chaogangword[k] += 1
            else:
                chaogangword[k] = 0
            #print j,k
chaogangword = sorted(chaogangword.iteritems(), key = lambda e:e[1], reverse = True)
print chaogangword
pindagang = [x / len(nxx[i]) for i,x in enumerate(indagang)]
plt.plot(1980*np.ones(33)+range(33),pindagang,'o-', alpha = 0.5)

#plt.plot(1980*np.ones(33)+range(33),llen,'r--o',alpha = 0.5)
#plt.axis([1979, 2013, 190, 1700])
plt.grid()
#plt.hold(True)
#plt.plot(1980*np.ones(33)+range(33),lw,'o-', alpha = 0.5)
#plt.show()

print len(list(set(otherwordlist))),list(set(otherwordlist))
