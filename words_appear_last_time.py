#coding=gbk
import wordEachyear as wy

es = range(32)#相同词汇数
esr1 = range(32)#以两年平均词汇数为基准
esr2 = range(32)#以当年
esr3 = range(32)#以上一年
for i in range(32):
    es[i] = len(set(wy.eywords[i]) & set(wy.eywords[i+1]))
    esr1[i] = float(es[i]) * 2 / (wy.eywords_volume[i] + wy.eywords_volume[i+1])
    esr2[i] = float(es[i]) / wy.eywords_volume[i+1]
    esr3[i] = float(es[i]) / wy.eywords_volume[i]

