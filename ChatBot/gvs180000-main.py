'''
Author: Gabriela Saenz
CS 4395.001
Fall 2022 @ University of Texas at Dallas
Portfolio Assignment Web Crawler
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import PySimpleGUI as sg
from tkinter import *
import threading
from processData import getTranscript
from scrapeData import getCorpus

sg.Window(title="AvatarBot", layout=[[]], margins=(100,50)).read()

avatarBot = ChatBot('AvatarBot',
                    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
                    logic_adapters=['chatterbot.logic.BestMatch'])

trainer1 = ChatterBotCorpusTrainer(avatarBot)
trainer1.train('chatterbot.corpus.english.greetings',
               'chatterbot_corpus\data\BotProfile.yml')

transcript1 = getTranscript()
trainer2 = ListTrainer(avatarBot)
trainer2.train(transcript1)

transcript2 = getCorpus()
trainer3 = ListTrainer(avatarBot)
trainer3.train(transcript2)

layout = [[sg.Multiline(size=(80, 20), reroute_stdout=True, echo_stdout_stderr=True)],
          [sg.MLine(size=(70, 5), key='-MLINE IN-', enter_submits=True, do_not_clear=False),
           sg.Button('SEND', bind_return_key=True), sg.Button('EXIT')]]

window = sg.Window('Chat Window', layout,
            default_element_size=(30, 2))


event, values = window.read()
print("Flame-o Hotman! I am the AvatarBot. I love all things Avatar: the Last Air Bender. What's your name?")
name = values['-MLINE IN-'].rstrip()
print(f"Good to see you {name}! How are you?")
#exit_conditions = [":q", "quit", "exit", "goodbye", "bye"]

while True:
    event, values = window.read()
    if event != 'SEND':
        print('Bye!')
        break
    string = values['-MLINE IN-'].rstrip()
    print('You:  ', string)
    # send the user input to chatbot to get a response
    response = avatarBot.get_response(values['-MLINE IN-'].rstrip())
    print('AvatarBot: ', response)

'''
print("Flame-o Hotman! I am the AvatarBot. I love all things Avatar: the Last Air Bender."
      "What's your name?")
exit_conditions = (":q", "quit", "exit", "goodbye", "bye")
while True:
    query = input("You: ")

    if query in exit_conditions:
        break
    else:
        print(f"AvatarBot: {avatarBot.get_response(query)}")
'''


