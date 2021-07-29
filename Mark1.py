import pyttsx3
import datetime as dt
import speech_recognition as sr

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
username = "User"
assname = "Mark 1"
def speak(Txt):
    engine.say(Txt)
    print(Txt)
    engine.runAndWait()
def greet():
    hour=dt.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
    speak(f"I am your Assistant {assname}")
def ask():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        audio=r.listen(source)

        try:
            command=r.recognize_google(audio,language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:
            print(e)
            speak("Sorry, I couldn't understand that.")
            return ""
        return command
greet()

while True:
    speak("How may I help you?")
    command = ask()
    if command == "":
        continue
    if "good bye" in command or "ok bye" in command or "stop" in command or "exit" in command:
        speak(f"Bye Bye, {assname} Shutting Down")
        break
    elif "what is your name" in command or "who are you" in command:
        speak(f"My name is {assname}")   
    elif "what is my name" in command or "do you know my name" in command:
        speak(f"Your name is {username}")
    elif "call me" in command or "change my name to" in command:
        command = command.replace("call me ","")
        command = command.replace("change my name to ","")
        username = command
        speak(f"From now onwards I will call you {username}")
    elif "change my name" in command:
            speak("What should i call you?")
            username = ask()
            while username =="":
                username = ask()
    elif "date" in command or "time" in command or "day" in command:
        if "day" in command or "date" in command:
            date = dt.datetime.today().strftime("%A %d %B %Y")
            speak(f"Today is {date}")
        if "time" in command:
            time = dt.datetime.today().strftime('%I:%M%p')
            speak(f"The time is {time}")
