import pyttsx3
import datetime
import os
import smtplib
import wolframalpha
from gtts import gTTS
from tkinter import *
from PIL import Image

import subprocess
import os
import sys
from PIL import Image, ImageTk


print("Hi enter your name")

def userstart():
    print("enter yoyr name")


user = input()    
def wishMe():
    print("Welcome my dear")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%m:%s")
    print(Time)
    print(date)
    print(month)
    print(year)
    print("the current time is")
    print(Time)
    print("the current date is")
    print(date)
    print(month)
    print(year)
    if hour>=6 and hour<12:
        print("Good Morning!" + user)
        print("Iam your assistant DoHu bot")

    elif hour>=12 and hour<18:
        print("Good Afternoon!" + user)
        print("Iam your assistant DoHu bot")

    elif hour>=18 and hour<24:
        print("Good Evening!" + user)
        print("Iam your assistant DoHu bot")

    else:
        print("Good night!" + user)
        print("Iam your assistant DoHu bot")

def assistant_print(output):
    global num

    #num to rename every message
if __name__ == "__main__":
    wishMe()
    while True:
        print("How can I help you")
        query = takeCommand().lower()  

if "who made you" in query:
    print("I have been cteated by DoHunger team, who areyoung developers")
    
elif "How can I call city hospital":
    print("Just call 145")
    
    
else:
    print("I couldn't find any information can you write it again" )    

