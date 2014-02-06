#coding=gbk
import wordEachyear as wy

'''
words_not_in_the_past
'''

words_not_in_the_past = range(33)
s = []

for i in range(33):
    words_not_in_the_past[i] = 0
for i in range(1,33):
    s += wy.eywords[i-1]
    for j in wy.eywords[i]:
        if j not in s:
            words_not_in_the_past[i] += 1

words_not_in_the_past[0] = wy.eywords_volume[0]