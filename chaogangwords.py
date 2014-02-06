#coding=gbk
import wordEachyear as wy
import dagangword as dw
import basicwords as bw
import numpy as np

notindagang = np.zeros(33)
chaogangword = {}
for j in range(33):
    for k in wy.eywords[j]:
        if k not in dw.dagangwords and k not in bw.basicwords:
            #notindagang[j] += 1
            if chaogangword.has_key(k):
                chaogangword[k] += 1
            else:
                chaogangword[k] = 1

for j in range(33):
    for k in wy.eywords[j]:
        if k not in dw.dagangwords and k not in bw.basicwords:
            if chaogangword[k] <= 2:
                notindagang[j] += 1
chaogangword = sorted(chaogangword.iteritems(), key = lambda e:e[1], reverse = True)
print 'Chaogangword =',chaogangword
pnotindagang = [float(x) / len(wy.eywords[i]) for i,x in enumerate(notindagang)]

