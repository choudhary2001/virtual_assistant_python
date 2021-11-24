import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 0 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Ai, Please tell me how may i help you..")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please ...")
        return "None"
    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 547)
    server.ehlo()
    server.starttls()
    server.login('youremail2001@gmail.com', 'Eadm@257545')
    server.sendmail('email@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedoia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Please, wait! Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Please, wait! Opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Please, wait! Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            speak("Please, wait! Opening github")
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\adras\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Please, wait! Opening Vscode")
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("What should I say??")
                content = takeCommand()
                to = "email@gmail.com"
                sendmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry bro!, I am not able to send the email.")
