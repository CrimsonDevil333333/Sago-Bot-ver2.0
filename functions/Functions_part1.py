#####  OPERATIONS INCLUDED  #####
# hi,Quit,joke

import random
from random import randrange
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5)
p=print

def hi():
    words_chat=("Hello sir","Hi","Hi sir")
    chat=random.choice(words_chat)
    engine.say(chat)
    print(chat)
    engine.runAndWait()
    
def Quit():
    quit_options=("ok bye","Hope to see you soon","See you soon","Thanks for giving your time")
    chat=random.choice(quit_options)
    engine.say(chat)
    print(chat)
    engine.runAndWait()
    engine.say("Please give us raitings from 1-10 stars")
    print("\nPlease give us raitings from 1-10 stars")
    engine.runAndWait()
    n=eval(input())
    ############################## feedback under work  ######################s

def joke():
    joke_options=("I dont want to",
                  "Britain has invented a new missile. Its called the civil servant - it doesnt work and it cant be fired.",
                  "What do you call an Englishman with an IQ of 50?  Colonel, sir.",
                  "Only in England...can a pizza get to your house faster than an ambulance.","Not now.")
    chat=random.choice(joke_options)
    engine.say(chat)
    print(chat)
    engine.runAndWait()

    
