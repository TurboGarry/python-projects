import pyttsx3

data = input("Enter the text you want to convert to speech: \n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()