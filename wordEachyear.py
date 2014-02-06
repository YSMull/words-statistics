#coding=gbk
import simplify_word as sw
import re
'''
eywords : words appear each year
eywords_volume : the volume of eywords
'''
eywords_volume = []
eywords = range(33)#sum of different words in every year
for i in range(33):
    filename = "data/%d.txt" % i
    infile = open(filename)
    wordsLists = []
    for eachLine in infile:
        wordsLists += [sw.simplify_word(word.lower()) 
                            for word in re.split("[^A-Za-z]", eachLine) 
                                if word != "" and word[-1].islower()]
    infile.close()
    
    freq_of_eachword = {}
    for word in wordsLists:
        freq_of_eachword[word] = 0
    for word in wordsLists:
        freq_of_eachword[word] += 1
        
    wordlist_order_by_freq = sorted(freq_of_eachword.iteritems(), key = lambda e:e[1], reverse = True)
    
    '''to ensure that the word appear at the head of a sentence 
    will not be treated differently, so first we turn each word to 
    lower state and second we use list(set()) multiple method which
    will eliminate iterative word ,to achieve that aim'''
    
    eywords[i] = list(set([p[0] for p in wordlist_order_by_freq]))
    eywords_volume.append(len(eywords[i]))

