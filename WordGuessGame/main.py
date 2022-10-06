'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Chapter 5: Word Guess Game
'''

import sys
import os
import nltk
import random
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from random import seed
from random import randint

def lexicalDiversity(txt):
    tokens = word_tokenize(txt)
    uniqueTokens = len(set(tokens))
    totalTokens = len(tokens)
    return (uniqueTokens/totalTokens)

def processText(txt):
    tokens = word_tokenize(txt) #tokenize words
    #tokens = [t.lower() for t in tokens]
    tokenLen = len(tokens) #length, for all tokens
    #tokens are only words of length greater than 5, that are not stopwords
    tokens = [t.lower() for t in tokens if t.isalpha() and
              t not in stopwords.words('english') and
              len(t) > 5]
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens] #get the lemmmas
    lemmas_unique = list(set(lemmas)) #get unique lemmas
    tags = nltk.pos_tag(lemmas)
    tagsUnique = nltk.pos_tag(lemmas_unique)
    print(f'First 20 unique tags:\n{tagsUnique[:20]}') #output first 20 unique tags
    #nounsUnique = [t[0] for t in tagsUnique if t[1].startswith('N')]
    nouns = [t[0] for t in tags if t[1].startswith('N')]
    nounsLen = len(nouns) #length, for only nouns
    print(f'\nNumber of tokens ({tokenLen}) Number of Nouns ({nounsLen})')

    #create a dictionary
    # key = noun
    # value = count of noun in list
    nounDict = {}
    for n in nouns:
        nounDict[n] = nouns.count(n)

    #sort the Dictionary from most to least occurrences
    nounDict = sorted(nounDict.items(), key = lambda x:x[1], reverse = True)
    #print the 50 most common words and their counts
    print(f'\nTop 50 most common words:\n{nounDict[:50]}')
    top50 = [n[0] for n in nounDict[:50]]
    return(top50)

def guessingGame(words):

    #Player starts with 5 points
    points = 5
    #number of rounds played
    rounds = 0
    #Flag for whether or not a new round should start
    gameOver = False

    while not gameOver:
        if rounds > 0:
            print("\nGuess another word")
        else:
            print("\nLet's play a word guessing game!") #Say at start of game


        keepPlaying = True #flag for playing or not playing a single round
        #Randomly choose one of the top50 words
        goal = words[randint(0,50)] #goal word

        #Output an "underscore space" for each letter in the word
        guess = ['_'] * len(goal)
        for g in guess:
            print(g[0], end = " ")

        while points >= 0 and keepPlaying: #start guessing
            letter = input("\nGuess a letter: ") #ask the user for a letter
            if letter in goal:
                points += 1
                indexNotFound = True
                index = goal.index(letter)
                while indexNotFound:
                    #check for empty space
                    if guess[index] == '_':
                        finalIndex = index
                        indexNotFound = False
                    else: #look for next instance of letter
                        index = goal.index(letter, index+1, len(goal))

                guess[finalIndex] = letter
                print(f"Right! Score is {points}")
                for g in guess:
                    print(g[0], end = " ")

                if all(g[0].isalpha() for g in guess):
                    print("\nYou solved it!")
                    print(f"\nCurrent score: {points}")
                    keepPlaying = False

            elif letter == "!": #chose to end game
                keepPlaying = False
                gameOver = True
            else: #guessed incorrectly
                points -= 1
                print(f"Sorry, guess again. Score is {points}")
                for g in guess:
                    print(g[0], end = " ")

        #end of guessing


        if points < 0:
            print("\n\nGame Over\n")
            gameOver = True

    #end of round

    print("\nThanks for playing!")

#gameOver


def file_method():

    if len(sys.argv) > 1:
        arg_input = sys.argv[1]
        with open(os.path.join(os.getcwd(), arg_input), 'r') as f:
            text_in = f.read()
        return text_in
    else:
        print("Did not enter sys arg")
        exit(-1) #User did not specify sysarg. End the program



if __name__ == '__main__':
    text_in = file_method() #fetch and check open file, returns text from data file
    lex = lexicalDiversity(text_in)
    print("\nLexical Diversity: %.2f\n" % lex)
    top50 = processText(text_in)
    guessingGame(top50)


