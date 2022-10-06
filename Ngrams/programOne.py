'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Chapter 8: Ngrams
'''

import sys
import os
import nltk
import pickle
from  nltk import word_tokenize
from nltk.util import ngrams

def nGrams_func(arg_input):
    #arg_input = input("Enter a training file: ") #prompt user for training file
    f = open(arg_input, 'r', encoding = "utf8") #open file
    text_in = f.read() #read text
    f.close() #close file

    text = text_in.replace('\n', ' ') #remove newlines
    unigrams = word_tokenize(text) #create unigrams list
    bigrams = list(ngrams(unigrams, 2)) #create bigrams list

    #Dictionaries: key = ngram, value = count
    unigram_dict = {t:unigrams.count(t) for t in set(unigrams)}
    bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}
    return unigram_dict, bigram_dict

if __name__ == '__main__':
    #English Dictionary
    arg_input = input("Enter a training file: ")  # prompt user for training file
    uni_dict_english, bi_dict_english = nGrams_func(arg_input)
    pickle.dump(uni_dict_english, open('uni_dict_english.p', 'wb'))
    pickle.dump(bi_dict_english, open('bi_dict_english.p', 'wb'))
    #French Dictionary
    arg_input = input("Enter a training file: ")  # prompt user for training file
    uni_dict_french, bi_dict_french = nGrams_func(arg_input)
    pickle.dump(uni_dict_french, open('uni_dict_french.p', 'wb'))
    pickle.dump(bi_dict_french, open('bi_dict_french.p', 'wb'))
    #Italian Dictionary
    arg_input = input("Enter a training file: ")  # prompt user for training file
    uni_dict_italian, bi_dict_italian = nGrams_func(arg_input)
    pickle.dump(uni_dict_italian, open('uni_dict_italian.p', 'wb'))
    pickle.dump(bi_dict_italian, open('bi_dict_italian.p', 'wb'))
