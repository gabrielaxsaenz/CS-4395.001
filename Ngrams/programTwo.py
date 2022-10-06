'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Chapter 8: Ngrams
'''

import nltk
import pickle
from nltk import word_tokenize
from nltk.util import ngrams

def compute_prob():
    testFile = open('LangId.test', 'r') #open test file
    testText = testFile.read() #read
    text = testText.split('\n') #separate lines


    i = 1
    f = open('probabilities.txt', 'w').close() #open txt file
    #calculate the probabilities of each language for each line
    for eachLine in text:
        unigrams_test = word_tokenize(eachLine)
        bigrams_test = list(ngrams(unigrams_test, 2))

        english_uni = pickle.load(open('uni_dict_english.p', 'rb'))
        french_uni = pickle.load(open('uni_dict_french.p', 'rb'))
        italian_uni = pickle.load(open('uni_dict_italian.p', 'rb'))

        vocabSize = len(english_uni)+ len(french_uni) + len(italian_uni)

        english_bi = pickle.load(open('bi_dict_english.p', 'rb'))
        french_bi = pickle.load(open('bi_dict_french.p', 'rb'))
        italian_bi = pickle.load(open('bi_dict_italian.p', 'rb'))

        p_english = 1
        p_french = 1
        p_italian = 1


        for bigram in bigrams_test:
            n_eng = english_bi[bigram] if bigram in english_bi else 0
            d_eng = english_uni[bigram[0]] if bigram[0] in english_uni else 0
            p_english = p_english * ((n_eng+1)/(d_eng+vocabSize))

            n_french = french_bi[bigram] if bigram in french_bi else 0
            d_french = french_uni[bigram[0]] if bigram[0] in french_uni else 0
            p_french = p_french * ((n_french+1)/(d_french+vocabSize))

            n_italian = italian_bi[bigram] if bigram in italian_bi else 0
            d_italian = italian_uni[bigram[0]] if bigram[0] in italian_uni else 0
            p_italian = p_italian * ((n_italian+1)/(d_italian+vocabSize))

            #assign the language with the highest probability
            p_list = [p_english, p_french, p_italian]
            p_largest = max(p_list)
            language = ""
            if p_list.index(p_largest) == 0:
                language = "English"
            elif p_list.index(p_largest) == 1:
                language = "French"
            else:
                language = "Italian"

        f = open('probabilities.txt', 'a+') #write each line to the file
        f.write(f'{i} {language}\n')
        i += 1
        f.close()
    testFile.close()

def accuracy():
    solFile = open('LangId.sol', 'r')  # open solutions file
    resultFile = open('probabilities.txt', 'r') #open test file

    #read files
    resultText = resultFile.read()
    solText = solFile.read()
    #split each line
    result = resultText.split('\n')
    solution = solText.split('\n')

    #list of indecies with incorrectly classified items
    wrongList = []
    correct = 0

    for (solLine, resultLine) in zip(solution, result):
        #test tokens
        s = word_tokenize(solLine)
        r = word_tokenize(resultLine)
        if len(s) > 0:
            solLang = s[1]
            resultLang = r[1]
            if solLang == resultLang:
                correct += 1
            else:
                wrongList.append(r[0])

    percentage = (correct/300) * 100
    print(f'Accuracy Percentage: {percentage}%\n')
    print(f'Accuracy: {(correct/300)}\n')
    print(f'Line numbers of incorret classifications: {wrongList}')


if __name__ == '__main__':
    compute_prob()
    print("Output file is probabilities.txt\n")
    accuracy()