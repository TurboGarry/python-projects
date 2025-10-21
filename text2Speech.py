import pyttsx3

# data = input("Enter the text you want to convert to speech: ")

engine = pyttsx3.init()
engine.say("hello world")
engine.runAndWait()