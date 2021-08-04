import pyttsx3
import datetime as dt
import speech_recognition as sr
import wolframalpha as wa
import os
import webbrowser as wb
import random
import requests as req
import json
from googlesearch import search
from time import sleep
import wikipedia as wiki
from PyDictionary import PyDictionary as dict

try:
    with open('data.json', 'r') as openfile:
        data = json.load(openfile)
    voice = data["voice"]
    username = data["username"]
    assname = data["assname"]
except:
    voice = 17
    username = "User"
    assname = "Mark 6"

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice].id)


def speakprint(txt):
    engine.say(txt)
    print(txt)
    engine.runAndWait()


def speak(txt):
    engine.say(txt)
    engine.runAndWait()


def changevoice():
    voiceid = [0, 7, 10, 16, 17, 26, 28, 32, 35, 36, 38, 39]
    speakprint("Choose a voice:")

    while True:
        for y in voiceid:
            select = True
            name = voices[y].name
            engine.setProperty('voice', voices[y].id)
            print(y)
            speakprint(f"Hello my name is {name}, I am your Personal Assistant")
            while select:
                select = bool(input("To select this voice press any letter than enter otherwise just enter: "))
                if select:
                    return y


def greet():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        speakprint("Hello,Good Morning " + username)
    elif 12 <= hour < 18:
        speakprint("Hello,Good Afternoon " + username)
    else:
        speakprint("Hello,Good Evening " + username)
    speakprint(f"I am your Assistant {assname}")


def ask():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        audio = r.listen(source)

        try:
            cmd = r.recognize_google(audio, language='en-in')
            print(f"user said:{cmd}\n")

        except Exception as error:
            print(error)
            speakprint("Sorry, I couldn't understand that.")
            return ""
        return cmd


greet()

while True:
    speakprint("How may I help you?")
    command = ask().lower()
    if command == "":
        continue
    if "good bye" in command or "bye" in command or "stop" in command or "exit" in command or "shutdown" in command:
        speakprint(f"Bye Bye, {assname} Shutting Down")
        break
    elif "sleep" in command and "go" in command:
        speak("For how long?")
        print("For how long(sec)")
        x = ask()
        while x == "":
            speak("Say that again")
            print("For how long(sec)")
            x = ask()
        num = []
        for y in x.split():
            if y.isdigit():
                num.append(y)
        speakprint(f"Going to sleep for {num[0]} sec")
        sleep(int(num[0]))
    elif "what is your name" in command or "who are you" in command:
        speakprint(f"My name is {assname}")
    elif "change your name" in command:
        speakprint("What will you like to call me")
        assname = ask()
        while assname == "":
            assname = ask()
        speakprint(f"From now onwards my name is {assname}")
    elif "what is my name" in command or "do you know my name" in command:
        speakprint(f"Your name is {username}")
    elif "call me" in command or "change my name to" in command:
        command = command.replace("call me ", "")
        command = command.replace("change my name to ", "")
        username = command
        speakprint(f"From now onwards I will call you {username}")
    elif "change my name" in command:
        speakprint("What should i call you?")
        username = ask()
        while username == "":
            username = ask()
        speakprint(f"From now onwards I will call you {username}")
    elif "on a date" in command:
        speakprint(random.choice(["I will rather deactivate then go out with you", "Nah I'm good"]))
    elif "date" in command or "time" in command or "day" in command:
        if "day" in command or "date" in command:
            date = dt.datetime.today().strftime("%A %d %B %Y")
            speakprint(f"Today is {date}")
        if "time" in command:
            time = dt.datetime.today().strftime('%I:%M%p')
            speakprint(f"The time is {time}")
    elif "calculate" in command:
        command = command.replace("calculate ", "")
        app_id = "EVYHEV-GP3W4RJPA5"
        client = wa.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        speakprint(ans)
    elif "ask" in command:
        speakprint('I can answer to computational and geographical questions and what question do you want to ask now')
        command = ask()
        app_id = "EVYHEV-GP3W4RJPA5"
        client = wa.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        speakprint(ans)
    elif "open" in command:
        if "chrome" in command or "google" in command:
            os.system("open /Applications/Google\ Chrome.app")
        elif "utorrent" in command and ".com" not in command:
            os.system("open /Applications/uTorrent.app")
        else:
            command = command.replace("open ", "")
            if ".com" not in command and os.path.exists(f"/Applications/{command}.app"):
                app = command.replace(" ", "\ ")
                os.system(f"open /Applications/{app}.app")
            else:
                site = command.replace(".com", "")
                site = site.replace(" ", "")
                url = f"https://www.{site}.com/"
                wb.open(url)
            speakprint(f"opening {command}")
    elif "change voice" in command or "change your voice" in command:
        voice = changevoice()
        greet()
    elif "good morning" in command or "good evening" in command or "good afternoon" in command:
        greet()
    elif "hello" in command or "hi" in command or "hey" in command:
        speakprint(random.choice(["Hello", "Hi", "Hey", "Bonjour", "Hiya"]))
    elif "you single" in command or "you married" in command:
        speakprint(random.choice(["I am single", "I'm married to the idea of helping people",
                                  "I'm Happy to say i feel whole all on my own\nPlus, I never have to share my desert",
                                  "I wanna keep that private \n\"PRIVACY\""]))
    elif "marry me" in command:
        speakprint(random.choice(
            ["NO", "I will rather deactivate then marry you", "Sorry not POSSIBLE", "LOL"
                                                                                    "\N{rolling on the floor laughing} "
                                                                                    "NO"]))
    elif "how are you" in command:
        speakprint(random.choice(["I am Fine", "I am doing great", "I'm happy to be here", ]))
    elif "am i hot" in command:
        speakprint(random.choice(["Hot as a tin roof under the sun", "Sorry I don't have a thermometer"]))
    elif "weather" in command:
        speakprint("Weather of which City?")
        city = ask()
        app_id = "a786c740192c5d9c2cab10255c49ef33"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}&units=metric"
        res = req.get(url)
        ans = res.json()
        if ans["cod"] != 404:
            temp = ans["main"]["temp"]
            humidity = ans["main"]["humidity"]
            des = ans["weather"][0]["main"]
            temph = ans["main"]["temp_max"]
            templ = ans["main"]["temp_min"]
            feel = ans["main"]["feels_like"]
            print("Temp:", temp, "ªC")
            print("High:", temph, "ªC Low:", templ, "ªC")
            print("Feels like:", feel, "ªC")
            print("Humidity:", humidity)
            print("Description:", des)
            speak(f"Its {des} The Temperature is {temp}degrees, with an high of {temph} and a low of {templ}, "
                  f"Due to the current Humidity it feels like {feel}degrees")
        else:
            speakprint("City Not Found")
    elif "make" in command and "note" in command:
        f = open("Note.txt", "w")
        cmd = "n"
        datetime = dt.datetime.today().strftime("%A %d %B %Y %I:%M%p")
        # noinspection PyUnboundLocalVariable
        while "n" in cmd or text == "" or "don't" in cmd:
            speakprint("What should i Write?")
            text = ask()
            print(text)
            speak("Should i save it")
            cmd = ask().lower()
        f.write(datetime + " " + text)
        f.close()
    elif "read" in command and "note" in command:
        try:
            f = open("Note.txt", "r")
            print("Your Note:", f.read())
            speak("Your Note")
            f.close()
        except:
            speakprint("You don't have any note")
    elif 'delete' in command and "note" in command:
        try:
            os.remove("Note.txt")
            speakprint("Note Deleted")
        except:
            speakprint("You don't have any note")
    elif "news" in command or "headline" in command:
        api_id = "f06509ec428d41f1b3e4824b273b1e10"
        url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_id}"
        res = req.get(url)
        ans = res.json()
        try:
            x = 0
            for news in ans["articles"]:
                title_news = news["title"]
                des_news = news['description']
                url_news = news['url']
                source = news["source"]["name"]
                speakprint("Top Headlines for you:")
                print(title_news)
                print(des_news)
                print("See more:", url_news)
                x += 1
                if x == 4:
                    speak(f'{title_news.replace(f"- {source}", "")} ')
                    break
                else:
                    speak(f'{title_news.replace(f"- {source}", "")} and,')
        except Exception as e:
            print(e)
            speakprint("No New News")
    elif "define" in command or ("what does" in command and "means" in command):
        command = command.replace("define ", "")
        defi = dict.meaning(command, disable_errors=True)
        try:
            x = 1
            noun = defi["Noun"]
            print("Noun:")
            speak("as an noun it means")
            for y in noun:
                if x == 1:
                    speakprint(f"{x}.\n{y}")
                else:
                    print(f"{x}.\n{y}")
                x += 1
        except:
            pass
        try:
            verb = defi["Verb"]
            print("Verb:")
            speak("as a verb it means")
            x = 1
            for y in verb:
                if x == 1:
                    speakprint(f"{x}.\n{y}")
                else:
                    print(f"{x}.\n{y}")
                x += 1
        except:
            pass
        try:
            adj = defi["Adjective"]
            print("Adjective:")
            speak("as an adjective it means")
            x = 1
            for y in adj:
                if x == 1:
                    speakprint(f"{x}.\n{y}")
                else:
                    print(f"{x}.\n{y}")
                x += 1
        except:
            pass
        sleep(10)
    elif "wikipedia" in command:
        command = command.replace("wikipedia ", "")
        print(wiki.summary(command, sentences=3))
        speak(wiki.summary(command, sentences=1))
    else:
        try:
            print("On the Web:")
            for res in search(command, start=0, stop=5, pause=2):
                print(res)
            speak("Here are some results i found on the Web")
        except:
            speakprint("Sorry I can't do that")

    
data = {
    "username": username,
    "assname": assname,
    "voice": voice
}
with open("data.json", "w") as outfile:
    json.dump(data, outfile)
