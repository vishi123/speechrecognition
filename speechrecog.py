# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:28:12 2019

@author: Manvi Gupta
"""

import speech_recognition as sr
#import pyaudio
r=sr.Recognizer()

with sr.Microphone() as source:
    print("SAY SOMETHING PLEASE");
    audio=r.listen(source)
    print("TIME OVER, THANKS");
    
try:
  print("TEXT: " + r.recognize_google(audio));#, language='hi-IN'));
except:
  pass;     
        