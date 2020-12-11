# import pyttsx3
# import datetime
# import speech_recognition as sr
# import pyjokes
# import wikipedia 
# import webbrowser
# import os 
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
# from twilio.rest import Client
# from clint.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
        
    elif hour >=12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
        
def intro():
    speak("I am Ciraai, how may i help you DEAR....")

    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        speak('listening...')
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print('recognizing...')
        query=r.recognize_google(audio)
        print("user said:",(query))
        
    except Exception as e:
        print(e)
        speak("i'm sorry didn't get ya...")  
        return "none"
    return query

        
    
    
    
        

if __name__=="__main__":
    clear = lambda: os.system('cls')
    
    clear()
    intro()
    wishMe()
    if True:
        query=takeCommand().lower() 
        
        
        if 'wikipedia' in  query: 
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'google' in query:
            webbrowser.open("google.com")
            
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/cyril_raju_/?hl=en") 
             
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
            speak("cheerup!....there is no time like present..")
              
        elif 'visual studio' in query:
            codepath="C:\\Users\\gargr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'joke' in query:
            joke=pyjokes.get_joke(language='en',category='all')
            speak(joke)
            print(joke)
            
            
        # some basic stuff
      
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, dear")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("CIRAAI")
            print("My friends call me CIRAAI")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by THE SWEETEST MISS RISHIKA...")
            
            
        elif "will you be my gf" in query or "will you be my " in query:   
            speak("I'm not sure about, may be you should give me some time")
            
        # elif "calculate" in query: 
             
        #     app_id = "Wolframalpha api id"
        #     client = wolframalpha.Client(app_id)
        #     indx = query.lower().split().index('calculate') 
        #     query = query.split()[indx + 1:] 
        #     res = client.query(' '.join(query)) 
        #     answer = next(res.results).text
        #     print("The answer is " + answer) 
        #     speak("The answer is " + answer) 
 
            
        #elif 'email to' in query: 
        #you can make a dictionary with name as placeholder and email address as key values
            # try:
            #     speak("what is the message you want to send?")
            #     content=takeCommand()
            #     to="gargrishika05@gmail.com"
            #     sendEmail(to,content)
            #     speak("email has been sent...")
            
            # except Exception as e:
            #     print(e)
            #     speak("sorry dear...i couldn't send the mail")