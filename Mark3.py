import pyttsx3
import datetime as dt
import speech_recognition as sr
import wolframalpha as wa
import os
import webbrowser as wb
import random

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)
username = "Muzammil"
assname = "Mark 3"


def speak(txt):
    engine.say(txt)
    print(txt)
    engine.runAndWait()


def changevoice():
    voiceid = [0, 7, 10, 16, 17, 26, 28, 32, 35, 36, 38, 39]
    speak("Choose a voice:")

    while True:
        for x in voiceid:
            select = True
            name = voices[x].name
            engine.setProperty('voice', voices[x].id)
            print(x)
            speak(f"Hello my name is {name}, I am your Personal Assistant")
            while select:
                select = bool(input("To select this voice press any letter than enter otherwise just enter: "))
                if select:
                    return voices[x]


def greet():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning " + username)
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon " + username)
    else:
        speak("Hello,Good Evening " + username)
    speak(f"I am your Assistant {assname}")


def ask():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        audio = r.listen(source)

        try:
            cmd = r.recognize_google(audio, language='en-in')
            print(f"user said:{cmd}\n")

        except Exception as e:
            print(e)
            speak("Sorry, I couldn't understand that.")
            return ""
        return cmd


greet()

while True:
    speak("How may I help you?")
    command = ask().lower()
    if command == "":
        continue
    if "good bye" in command or "bye" in command or "stop" in command or "exit" in command:
        speak(f"Bye Bye, {assname} Shutting Down")
        break
    elif "what is your name" in command or "who are you" in command:
        speak(f"My name is {assname}")
    elif "change your name" in command:
        speak("What will you like to call me")
        assname = ask()
        while assname == "":
            assname = ask()
        speak(f"From now onwards my name is {username}")
    elif "what is my name" in command or "do you know my name" in command:
        speak(f"Your name is {username}")
    elif "call me" in command or "change my name to" in command:
        command = command.replace("call me ", "")
        command = command.replace("change my name to ", "")
        username = command
        speak(f"From now onwards I will call you {username}")
    elif "change my name" in command:
        speak("What should i call you?")
        username = ask()
        while username == "":
            username = ask()
        speak(f"From now onwards I will call you {username}")
    elif "on a date" in command:
        speak(random.choice(["I will rather deactivate then go out with you", "Nah I'm good"]))
    elif "date" in command or "time" in command or "day" in command:
        if "day" in command or "date" in command:
            date = dt.datetime.today().strftime("%A %d %B %Y")
            speak(f"Today is {date}")
        if "time" in command:
            time = dt.datetime.today().strftime('%I:%M%p')
            speak(f"The time is {time}")
    elif "calculate" in command:
        command = command.replace("calculate ", "")
        app_id = "EVYHEV-GP3W4RJPA5"
        client = wa.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        speak(ans)
    elif "ask" in command:
        speak('I can answer to computational and geographical questions and what question do you want to ask now')
        command = ask()
        app_id = "EVYHEV-GP3W4RJPA5"
        client = wa.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        speak(ans)
    elif "open" in command:
        if "chrome" in command or "google" in command:
            os.system("open /Applications/Google\ Chrome.app")
        elif "utorrent" in command:
            os.system("open /Applications/uTorrent.app")
        else:
            command = command.replace("open ", "")

            if ".com" not in command and os.path.exists(f"/Applications/{command}.app"):
                app = command.replace(" ", "\ ")
                os.system(f"open /Applications/{app}.app")
            else:
                site = command.replace(".com", "")
                url = f"https://www.{site}.com/"
                wb.open(url)
            speak(f"opening {command}")
    elif "change voice" in command or "change your voice" in command:
        voice = changevoice()
        greet()
    elif "good morning" in command or "good evening" in command or "good afternoon" in command:
        greet()
    elif "hello" in command or "hi" in command or "hey" in command:
        speak(random.choice(["Hello", "Hi", "Hey", "Bonjour", "Hiya"]))
    elif "you single" in command or "you married" in command:
        speak(random.choice(["I am single", "I'm married to the idea of helping people",
                             "I'm Happy to say i feel whole all on my own\nPlus, I never have to share my desert",
                             "I wanna keep that private \n\"PRIVACY\""]))
    elif "marry me" in command:
        speak(random.choice(
            ["NO", "I will rather deactivate then marry you", "Sorry not POSSIBLE", "LOL"
                                                                                    "\N{rolling on the floor laughing} "
                                                                                    "NO"]))
    elif "how are you" in command:
        speak(random.choice(["I am Fine", "I am doing great", "I'm happy to be here", ]))
