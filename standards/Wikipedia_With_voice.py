import wikipedia
import pyttsx3
from database.data_base import *
p=print
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5)

def wiki():
    flag=True
    try:
        engine.say("what ever you want to search in wikipedia you can ask me")
        p("what ever you want to search in wikipedia you can ask me")
        engine.runAndWait()
        while (flag==True):
            engine.say('what do you want to know')
            engine.runAndWait()
            n=input("what do you want to know ---> ")
            wikipedia_search(n)
            if(n=='quit' or n=='exit' or n=="QUIT" or n=="EXIT" or n=="Nothing" or n=="Quit" or n=="nothing" or n=="Exit"):
                p("\nHope to see you Again\nThanks for giving us your precious time")
                engine.say('Hope to see you Again')
                engine.runAndWait()
                engine.say("Thanks for giving us your precious time")
                engine.runAndWait()
                flag=False
            else:
                q=wikipedia.summary(n, sentences=3)
                engine.say(q)
                p("\n",q)
                engine.runAndWait()
                p("\n\n")
    except:
            print("You are not connected to Internet\nPlease try again latter")
  
        
    
        
    




