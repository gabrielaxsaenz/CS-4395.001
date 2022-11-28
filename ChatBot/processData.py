import pandas as pd
from nltk import sent_tokenize
from nltk import word_tokenize

def makeConvo(fileName):

    characterNames = ['Katara', 'Sokka', 'Aang', 'Zuko', 'Iroh', 'Village Girl', 'Kanna',
                      'Southern Water Tribe boy', 'Village boy']
    with open(fileName) as f:
        lines = [line.rstrip() for line in f]

    i = 0
    for line in lines:

        words = word_tokenize(line)

        words = [w for w in words if w not in characterNames and
                   w.isalpha() or w == '.']

        newLine = ''
        for w in words:
            if w == '.':
                newLine += str(w)
            else:
                newLine += ' '+str(w)
        lines[i] = newLine
        i+=1

    with open('convo.txt', 'w') as convo:
        convo.write(str(lines))

    return lines

def getTranscript():
    fileName = 'myfile.txt'
    with open('archive/transcript_1_1_The_Boy_in_the_Iceberg.csv', 'r') as f_in, open(fileName, 'w') as f_out:
        content = f_in.read().replace(',', ' ')
        f_out.write(content)
    transcript = makeConvo(fileName)
    return transcript

'''
if __name__ == '__main__':
    fileName = 'myfile.txt'
    with open('archive/transcript_1_1_The_Boy_in_the_Iceberg.csv', 'r') as f_in, open(fileName, 'w') as f_out:
        content = f_in.read().replace(',',' ')
        f_out.write(content)
    makeConvo(fileName)
'''