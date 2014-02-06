import wordEachyear as wy

'''
words_appear_every_year
'''
sset = range(33)
words_appear_all_the_time = set(wy.eywords[0])
for i in range(33):
    words_appear_all_the_time &= set(wy.eywords[i])
print words_appear_all_the_time