#coding=gbk
import matplotlib.pyplot as plt
import numpy as np
import wordEachyear as wy
import words_appear_all_the_time as waatt
import words_appear_last_time as walt
import not_in_past as nip
import chaogangwords as cgw

x33 = 1980*np.ones(33)+range(33)
x32 = 1981*np.ones(32)+range(32)

plt.figure('wordeachyear')
plt.plot(x33,wy.eywords_volume,'r--o',alpha = 0.5)
plt.grid(True)
plt.show()

plt.figure('notindagang')
plt.plot(x33,cgw.notindagang,'o-', alpha = 0.5)
plt.grid(True)
plt.show()

plt.figure('wn')
plt.plot(wy.eywords_volume,cgw.pnotindagang,'bo')
plt.show()


plt.figure('pchaogang')
plt.plot(x33,cgw.pnotindagang,'o-', alpha = 0.5)
plt.grid(True)
plt.show()

plt.figure('notinpast')
plt.bar(x33,nip.words_not_in_the_past, color = 'green', alpha = 0.5)
plt.grid(True)
plt.show()

plt.figure('wordsAppearLastTime')
plt.plot(x32, walt.es, 'b--o', alpha = 0.5)
plt.grid(True)
plt.show()

plt.figure('pwordsAppearLastTime')
#plt.axes([1980, 2013 , 0.35 ,0.6])
plt.plot(x32, walt.esr1, 'r-o')
plt.plot(x32, walt.esr2, 'b--o', alpha = 0.4)
plt.plot(x32, walt.esr3, 'y--o', alpha = 0.4)
plt.grid(True)

plt.show()
