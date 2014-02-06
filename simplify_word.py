#coding=gbk
import en

otherwordlist = []
def simplify_word(a):
    
    try:#测试是否为动词,如果是则返回
        en.is_verb(en.verb.present(a))
        return en.verb.present(a)
    except:#否则继续检查
        pass
    
    #测试是否是名词
    if en.is_noun(en.noun.singular(a)):
        return en.noun.singular(a)
    
    #如果已经可以判断是名词,动词,形容词,副词,连词
    if en.is_noun(a) or en.is_verb(a) or en.is_adjective(a) or en.is_adverb(a) or en.is_connective(a):
        return a
        
    
    
    
    otherwordlist.append(a)
    return a

    

