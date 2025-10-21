import pyttsx3
import speech_recognition as sr

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something.....")
        audio = r.listen(source)
        print("Done.")
    
    
