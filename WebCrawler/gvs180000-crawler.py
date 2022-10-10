'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Assignment Web Crawler
'''

import urllib
import requests
import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk import word_tokenize
import warnings
warnings.filterwarnings('ignore')
import pickle
from urllib import request
from bs4 import BeautifulSoup

def extractLinks(soup):

    #Extract 15 relevant links
    #page = requests.get(startURL)
    #html = request.urlopen(startURL).read().decode('utf8')
    #soup = BeautifulSoup(page.content, 'html.parser')
    #soup = BeautifulSoup(html)

    #extract links
    counter = 0
    links = []
    for link in soup.find_all('a'):
        counter += 1
        if counter > 30:
            break
        links.append(link.get('href'))
    #scrape text

    if None in links:
        links.remove(None)

    rel = [l for l in links if l.startswith('h')]
    relevant = rel[:15]

    return relevant

def scrapeText(relevant):
    i = 1
    txt = ""
    for r in relevant:
        page = requests.get(r)
        soup = BeautifulSoup(page.content, 'html.parser')
        #for p in soup.select('p'):
        #    txt = p.get_text()
            #print(txt)
        fileName = 'text-%s.txt' % i
        with open(fileName, 'w', encoding='utf-8') as f:
            for p in soup.select('p'):
                txt = p.get_text()
                #print(txt)
                f.write(txt)
            f.close()
        i += 1

def cleanText():
    #work with each file
    for i in range(1,16):
        fileName = 'text-%s.txt' % i
        textFile = open(fileName, 'r', encoding = "utf8") #open file
        text_in = textFile.read() #read text

        text = text_in.replace('\n', ' ') #remove newline
        text = text.replace('\t', ' ')#remove tabs
        sentences = sent_tokenize(text)
        sentFile = 'sent-%s.txt' % i
        sentFile = open(sentFile, 'w', encoding = "utf8") #create sentence file
        for s in sentences:
            sentFile.write(s)
        sentFile.close()
        textFile.close()

def extractTerms():
    #work with each file
    terms = []
    tf_dict = {}
    for i in range(1, 16):

        fileName = 'sent-%s.txt' % i
        sentFile = open(fileName, 'r', encoding = 'utf8') #open file
        sent_in = sentFile.read() #read sentences
        tokens = word_tokenize(sent_in)
        tokens = [t.lower() for t in tokens if t.isalpha() and
                  t not in stopwords.words('english')]
        for t in tokens:
            terms.append(t)

    #get term frequencies
    token_set = set(terms)
    tf_dict = {t:terms.count(t) for t in token_set}
    #normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t]/len(terms)
    dictSorted = sorted(tf_dict.items(), key = lambda x:x[1], reverse = True)
    print(f'Top40 terms extracted:\n {dictSorted[:40]}')

def searchKnowledge(key):
    print(knowledgeBase[key])

if __name__ == '__main__':
    startURL = "https://www.brothers-brick.com/"
    html = request.urlopen(startURL).read().decode('utf8')
    soup = BeautifulSoup(html)
    relevantLinks = extractLinks(soup)
    print(f'15 Relevant Links:\n {relevantLinks}')
    scrapeText(relevantLinks)
    cleanText()
    extractTerms()

    knowledgeBase = {"lego": "The Brothers Brick is a LEGO website for adult builders and fans of LEGO.",
                     "brick":"The Brothers Brick is funded by our readers and the community.",
                     "brothers":"Each month, hundreds of thousands of people read articles that "
                                "The Brothers Brick publishes.",
                     "new":"Depicting a weary samurai discovering a strange new land, this construction displays some "
                           "excellent prowess in natural and sculpted forms. ",
                     "world": "In addition to the amazing LEGO models created by builders all over the world, "
                              "The Brothers Brick brings you the best LEGO news and reviews.",
                     "set": "Get ready to take on your friends with this table-top football set complete with an entire"
                            " team – including benchwarmers.",
                     "star": "Fans of the Star Wars show The Mandalorian, on Disney’s streaming service, have a lot to "
                             "be excited about this week as we revealed and then reviewed the latest LEGO UCS Star Wars "
                             "set, the Razor Crest, which is the most screen accurate model since the Death Star (wink).",
                     "builder": " Builder Simon Liu, one of the founders of the SHIPtember prompt, has created yet "
                                "another masterpiece to add to the ranks of this year’s armada.",
                     "variety": " Each of the dozens of flowers adorning the grounds here feels unique, a single "
                                "beautiful piece in the larger puzzle. And the variety is outstanding, bounding between "
                                "building techniques with ease.",
                     "things": "But sometimes you’ve gotta appreciate the little things in life."}

    response = input("Search Knowledge Base?[y/n]")
    while response == 'y':
        key = input("The searchable terms are:\n"
                    "1. lego 2. brick 3. brothers 4. new 5. world 6. set 7. star"
                    "8. builder 9. variety 10. things\n"
                    "What term would you like to hear about?: ")
        searchKnowledge(key)
        response = input("Search another term?[y/n]")
    print("Thanks for chatting!")