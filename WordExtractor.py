#-*- coding: UTF-8 -*-
''' 
    @author: xmpy(Xiaoemng Zhao)
    @description: It is a simple tornado server which show the result of KeyWord Extraction
'''

import codecs
import datrie
import unicodedata
from operator import itemgetter
import re
import math


def find_next_punc(sentence):
    punc_index = -1
    for i in xrange(len(sentence)):
        if sentence[i] in '\n\t ' or unicodedata.category(sentence[i])[0] == 'P':
            return i
    return punc_index

class WordExtracter(object):
    """It is used to extract keywords from content"""
    trie = None
    stop_words = []

    ### trie_filepath is the dictionary path built by datrie.
    def __init__(self, trie_filepath):
        super(WordExtracter, self).__init__()
        self.trie = datrie.Trie.load(trie_filepath)

    ### add the list of stop words such as "the", "a", ...
    def initStopWords(self,stop_words_filepath):
        with codecs.open(stop_words_filepath,'r','utf-8') as f:
            for line in f:
                self.stop_words.append(line.strip())


    ### extract keywords from sentence
    def get_wiki_entities(self, sentence):
        result = {}
        idf_dict = {}
        while(1):
            try:
                word = self.trie.longest_prefix(sentence)
                if len(word) != len(sentence):
                    if not (sentence[len(word)] in '\n\t ' \
                            or unicodedata.category(sentence[len(word)])[0] == 'P'):
                        punc_index = find_next_punc(sentence[len(word):])
                        if punc_index == -1:
                            if sentence[len(word):] == "es" or sentence[len(word):] == "s":
                                result.setdefault(word,0)
                                idf_dict.setdefault(word, self.trie[word])
                                result[word] = result[word] + 1
                                return dict([(k, v*idf_dict[k]) for k,v in result.items() if not unicodedata.category(k[0])[0] == 'P'])
                            else:
                                return dict([(k, v*idf_dict[k]) for k,v in result.items() if not unicodedata.category(k[0])[0] == 'P'])                    
                        else:
                            if sentence[len(word):len(word)+punc_index] == "es" or sentence[len(word):len(word)+punc_index] == "s":
                                result.setdefault(word,0)
                                idf_dict.setdefault(word, self.trie[word])
                                result[word] = result[word] + 1
                                if punc_index == (len(sentence)- len(word) -1):
                                    return dict([(k, v*idf_dict[k]) for k,v in result.items() if not unicodedata.category(k[0])[0] == 'P'])
                                else:
                                    sentence=sentence[len(word)+punc_index+1:]
                                    continue
                            else:
                                punc_index = find_next_punc(sentence)
                                #if punc_index_2 != punc_index:    
                                sentence = sentence[punc_index+1:]
                                continue
                    else:
                        #print sentence
                        sentence = sentence[len(word)+1:]
                else:
                    result.setdefault(word,0)
                    idf_dict.setdefault(word, self.trie[word])
                    result[word] = result[word] + 1
                    return dict([(k, v*idf_dict[k]) for k,v in result.items() if not unicodedata.category(k[0])[0] == 'P'])
            except KeyError,e:
                #print"Exception sentence:", sentence
                punc_index = find_next_punc(sentence)
                if punc_index == -1 or punc_index == (len(sentence)-1):
                    return dict([(k, v*idf_dict[k]) for k,v in result.items() if not unicodedata.category(k[0])[0] == 'P'])
                else:
                    sentence = sentence[punc_index+1:]
                continue
            if word not in self.stop_words:
                result.setdefault(word,0)
                idf_dict.setdefault(word, self.trie[word])
                result[word] = result[word] + 1
            

if __name__ == "__main__":
    print find_next_punc(u"haah fdfa'")
    print find_next_punc(u"dafdf")

    a = u"North Carolina Lawmakers Hope to Even Road for Drivers By Charging Fees for Green Cars"
    a = a.lower()
    b = u"Vine, Twitter’s New Video Tool, Hits 13 Million Users"
    b = b.lower()
    ew = WordExtracter('my_small.trie')
    ew.initStopWords('stop_words')
    print sorted(ew.get_wiki_entities(a).iteritems(),key=itemgetter(1),reverse=True)
    print sorted(ew.get_wiki_entities(b).iteritems(),key=itemgetter(1),reverse=True)

    