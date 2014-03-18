#-*- coding: UTF-8 -*-
''' 
    @author: xmpy(Xiaoemng Zhao)
    @description: Given an dictionary, this script can buid an double array trie.
'''

import codecs
import pickle
import datrie
from time import time
import math


char_list = pickle.load(open('char_list.conf','rb'))
trie = datrie.Trie(u''.join(char_list))
n = 0
begin = time()

with codecs.open('1_2gram_idf','r','utf-8') as f:
    for line in f:
        cols = line.strip().split('\t')
        if len(cols) <  2:
            print line
            continue
        ent = cols[0]
        idf = float(cols[1])
        ent = ent.lower().replace('_',' ')
        trie[ent] = idf

trie.save('my_small.trie')
