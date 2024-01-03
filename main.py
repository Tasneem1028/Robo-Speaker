import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to RoboSpeaker created by Tasneem")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x=="q":
            break
        speak(x)




