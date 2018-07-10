#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:12:04 2018

@author: zhouh
"""
import csv
import numpy as np
import re
import nltk
from nltk.corpus import words
from nltk.corpus import stopwords
import nltk.tokenize as nt
import string
import os
from nltk.tag import StanfordPOSTagger

def readCSV(file):
    indata = []	
    with open(file, 'r') as dataIn:
        reader = csv.reader(dataIn)
        for row in reader:
            indata.append(row)
    return indata

def read_file(filename):
    with open(filename,'r') as f:
        text = f.read()
    return text

def getId(data,lang):
    all_data = filter(lambda x:x[2]==lang,data)
    video_id = []
    for i in all_data:
        v_id = re.search(r'\d+',i[0]).group()
        video_id.append(v_id)
    return video_id


def _max_match(text):    
    wordlist = set(words.words())
    wordnet_lemmatizer = nltk.WordNetLemmatizer()
    pos2 = len(text)
    result =''
    while len(text)>0:
        word = wordnet_lemmatizer.lemmatize(text[0:pos2])
        if word in wordlist:
            result = result + text[0:pos2] + ' '
            text =text[pos2:]
            pos2 = len(text)
        else:
            pos2 = pos2-1
    return result[0:-1]

def _preprpcessing_de(id_list):
    stop_w = set(stopwords.words('german'))
    de_tagger = StanfordPOSTagger(model_filename='/home/zhouh/Downloads/stanford-postagger-full-2018-02-27/models/german-ud.tagger',
                                  path_to_jar = '/home/zhouh/Downloads/stanford-postagger-full-2018-02-27/stanford-postagger.jar')
    for i in id_list:
        try:            
            text = read_file('/home/zhouh/Thesis/code/Transcripts/german/'+i+'.txt')
            words = nt.word_tokenize(text, language='german')
            word = [x for x in words if x not in string.punctuation]
            word = [x for x in word if x not in stop_w]
            word = [x for x in word if not x.isdigit()]
            word = de_tagger.tag(word)
            tt = ''
            for w in word:
                tt += '/'.join(w)+' '
                
            new_path = '/home/zhouh/Thesis/code/Transcripts/de_preprocessed/'+i+'pre.txt'
            if os.path.exists(new_path):
                os.remove(new_path)
            with open(new_path, 'w') as f:
                f.write(tt)
        except:
            continue

def _preprpcessing_eng(id_list):
    stop_w = set(stopwords.words('english')) 
    eng_tagger = StanfordPOSTagger(model_filename='/home/zhouh/Downloads/stanford-postagger-full-2018-02-27/models/english-bidirectional-distsim.tagger',
                               path_to_jar='/home/zhouh/Downloads/stanford-postagger-full-2018-02-27/stanford-postagger.jar')
            
    for i in id_list:
        try:                
            text = read_file('/home/zhouh/Thesis/code/Transcripts/english/'+i+'.txt')
            words = nt.word_tokenize(text, language='english')
            word = [x for x in words if x not in string.punctuation]
            word = [x for x in word if x not in stop_w]
            word = [x for x in word if not x.isdigit()]
            word = eng_tagger.tag(word)
            tt = ''
            for w in word:
                tt += '/'.join(w)+' '
            
            new_path = '/home/zhouh/Thesis/code/Transcripts/eng_preprocessed/'+i+'pre.txt'
            if os.path.exists(new_path):
                os.remove(new_path)
            with open(new_path, 'w') as f:
                f.write(tt)
        except:
            continue

all_meta = readCSV('/home/zhouh/Thesis/code/videoResources_complete.csv')
all_eng = getId(all_meta,'eng')
all_de = getId(all_meta,'ger')


#de_tagger = StanfordPOSTagger(model_filename='/home/zhouh/Downloads/stanford-postagger-full-2018-02-27/models/german-ud.tagger',
#                                  path_to_jar = '/home/zhouh/Downloads/stanford-postagger-full-2018-02-27/stanford-postagger.jar')
#print(de_tagger.tag('Das ist ein Test für die Übertragung'.split()))
#
#preprpcessing_eng(all_eng)

def main():
    _preprpcessing_de(all_de)
    
if __name__ == '__main__':
    main()

#intab = "0123456789"
#
#trantab = str.maketrans(intab)
#
#str1 = "this 4695 is string85 example....wow!!!"
#print (str1.translate(trantab))


#string='theyarebirds'
#test = max_match(words)