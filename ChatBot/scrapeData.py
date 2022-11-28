'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Assignment Web Crawler
'''

import requests
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords

def scrapeWiki():
    URL = 'https://en.wikipedia.org/wiki/Avatar:_The_Last_Airbender'

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()

    #for p in soup.select('p'):
    #    print(p.get_text())

    results = soup.findAll('div', {'snippet-item r-snippetized'})
    with open('wikiFile.txt', 'w') as f:
        for p in soup.select('p'):
            f.write(p.get_text())

def getCorpus():
    scrapeWiki()
    fileName = 'wikiFile.txt'
    terms = []

    sentFile = open(fileName, 'r', encoding='windows-1252')  # open file
    sent_in = sentFile.read()  # read sentences
    tokens = word_tokenize(sent_in)
    uselessWords = ['the', 'also', 'it', 'in']
    tokens = [t.lower() for t in tokens if t.isalpha() and
              t not in stopwords.words('english') and
              t not in uselessWords]
    for t in tokens:
        terms.append(t)

    # get term frequencies

    token_set = set(terms)
    tf_dict = {t: terms.count(t) for t in token_set}
    # normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(terms)
    dictSorted = sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)
    #print(f'Top40 terms extracted:\n {dictSorted[:40]}')

    knowledgeBase = {'avatar': "The only individual who can bend all four elements, the \"Avatar\", is responsible for maintaining harmony among the world's four nations, and serves as the bridge between the physical world and the spirit world.",
    'aang': "A century ago, young Avatar Aang, afraid of his new responsibilities, fled from his home and was forced into the ocean by a storm. He encased himself in suspended animation in an iceberg near the South Pole. Shortly afterward, Fire Lord Sozin, the ruler of the Fire Nation, launched a world war to expand his nation's empire.",
    ##'fire nation': "Aang's group travels to Ba Sing Se to seek the Earth King's support for an attack on the Fire Nation timed to an upcoming solar eclipse, during which firebenders will be powerless.",
    'world': "Avatar is set in an Asiatic-inspired world in which some people can telekinetically manipulate one of the four elements—water, earth, fire or air—through practices known as \"bending\", inspired by Chinese martial arts.",
    'zuko': 'Zuko—the exiled prince of the Fire Nation, seeking to restore his lost honor by capturing Aang, accompanied by his wise uncle Iroh—and later, his ambitious sister Azula.',
    'water': 'In the first season, Aang travels with Katara and Sokka to the Northern Water Tribe so he can learn waterbending and be prepared to defeat the Fire Nation.',
    'earth': 'In the second season, Aang learns earthbending from Toph Beifong, a blind twelve-year-old earthbending prodigy.',
    'airbender': 'Avatar: The Last Airbender is set in a world where human civilization consists of four nations, named after the four classical elements: the Water Tribes, the Earth Kingdom, the Fire Nation, and the Air Nomads.',
    'katara': 'A hundred years later, siblings Katara and Sokka, teenagers of the Southern Water Tribe, accidentally discover Aang and revive him.',
    'war': 'These include concepts rarely touched on in youth entertainment, including war, genocide, imperialism, totalitarianism, indoctrination and free choice.',
    'sokka': "Sokka is initially dismissive of the all-female Kyoshi Warriors, but learns to respect and appreciate their skills.[5] According to Kirk Hamilton of Kotaku, these themes represent the show's message that it is more important to be oneself than hew to societal expectations.",
    'Iroh': 'rince Zuko, the banished son of the current Fire Lord Ozai, pursues them, accompanied by his uncle Iroh, hoping to capture the Avatar in order to restore his honor.'}

    return knowledgeBase
