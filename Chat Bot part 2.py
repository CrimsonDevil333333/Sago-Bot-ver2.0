from difflib import get_close_matches
import pyttsx3
import os


from functions.Functions_part1 import *
from standards.Wikipedia_With_voice import *
from standards.calculator import *
from database.data_base import *
from database.reciver import *



p=print
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5)
n=True
def closeMatches(patterns, word): 
     n = get_close_matches(word, patterns)
     print("you asked According to me - ",n)
     try:
          ####################################
          if(n[0]=="what can you do"):     #
               engine.say("nothing for now") #
               print("nthing for now")       #
               engine.runAndWait()           #
          ####################################
          if(n[0]=="what is your name"):
               engine.say("My name is sago and i am your personal assistant")
               print("My name is sago and i am your personal assistant")
               engine.runAndWait()
          if(n[0]=='quit'):
               Quit()
          if(n[0]=='Open Wikipedia'):
               wiki()
          if(n[0]=='hi'):
               hi()
          if(n[0]=="can you tell me a joke"):
               joke()
          if(n[0]=="open calculator"):
               engine.say("Opening please wait")
               print("opening....")
               engine.runAndWait()
               root = Tk() 
               obj=calc(root)
               root.mainloop()
               print("Terminated")
     except:
          engine.say("please rephrase the statement")
          print("please rephrase the statement :)")
          engine.runAndWait()
          unknown_input(word)

def start():
     engine.say("I am your personal assistant I am here to assist you. please wait for a while")
     p("I am your personal assistant I am here to assist you\nPlease wt fr a while")
     engine.runAndWait()
if __name__ == "__main__":
    start()
    l=reader()
    Mail_Recever(l)
    initializing_database()
    while(n==True):
         word = input()
         database_input(word)
         patterns = ['what can you do','open calculator',
                     'what is your name',
                     'quit','Open Wikipedia',
                     'hi','can you tell me a joke'] 
         closeMatches(patterns, word) 
