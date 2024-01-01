import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia  
import webbrowser
import os
import smtplib
import pyjokes 
import time
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id) = david
engine.setProperty('voice', voices[0].id)

#api_key = "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"
#openai.api_key = api_key
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir ,Please tell me how may i help you")


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com','yourpass')
    server.sendmail('your@gmail.com',to,content)
    server.close()

def toDoList():
    # Get the to-do list from the user
    toDoList =speak("What do you want to add to your to-do list? ")

    # Add the to-do item to the list
    with open("toDoList.txt", "a") as f:
        f.write(toDoList + "\n")

    # Speak to the user that the to-do item has been added
    speak("The to-do item has been added.")
if __name__ == "__main__":
    wishMe()
    #if 1:
    while True:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral") 
            speak(My_joke)
            
        elif 'quit' in query:
            exit()
        elif 'what is time' in query:
            seconds = time.time()
            local_time = time.ctime(seconds)
            print("Local time:", local_time)


