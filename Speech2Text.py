import pyttsx3
import speech_recognition as sr

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something.....")
        audio = r.listen(source)
        print("Done.")
    
    try:
        text = r.recognize_google(audio)
        print("You Said : " + text)
    
    except Exception as Ep:
        print(Ep)

speech()