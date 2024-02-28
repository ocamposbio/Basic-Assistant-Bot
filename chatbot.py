import os
import random
import time
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import pywhatkit
import requests
import json
import pyautogui
import psutil
import pytz
import smtplib
from email.message import EmailMessage

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am BAT, your personal assistant. How may I help you?")
    speak("You can ask me anything.")

# Function to take the user's command
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Function to send an email
def send_email(to, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('')
    server.sendmail('')  # Add sender's email address and password
    server.quit()

# Main function
if __name__ == "__main__":
    greet()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow...")
            webbrowser.open("https://www.stackoverflow.com")
        elif 'play music' in query:
            speak("Playing music...")
            music_dir = 'C:\\Users\\user\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"The date is {strDate}")
        elif 'open code' in query:
            speak("Opening Visual Studio Code...")
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'search' in query:
            speak("What do you want to search for?")
            search = take_command().lower()
            speak(f"Searching for {search}...")
            webbrowser.open(f"https://www.google.com/search?q={search}")
        elif 'play' in query:
            speak("What do you want to play?")
            song = take_command().lower()
            speak(f"Playing {song}...")
            pywhatkit.playonyt(song)
        elif 'weather' in query:
            speak("What is the city name?")
            city = take_command().lower()
            api_key = "your_api_key"
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            weather_data = requests.get(base_url).json()
            if weather_data["cod"] != "404":
                weather = weather_data["main"]
                temperature = round(weather["temp"] - 273.15, 2)
                humidity = weather["humidity"]
                description = weather_data["weather"][0]["description"]
                speak(f"The temperature in {city} is {temperature} degrees Celsius with {description} and {humidity}% humidity.")
            else:
                speak("City not found.")
        elif 'screenshot' in query:
            speak("Taking screenshot...")
            screenshot = pyautogui.screenshot()
            screenshot.save("C:\\Users\\user\\Pictures\\screenshot.png")
            speak("Screenshot saved.")
        elif 'cpu' in query:
            usage = str(psutil.cpu_percent())
            speak(f"CPU is at {usage}%")
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            speak(f"Battery is at {battery.percent}%")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                speak("Who is the recipient?")
                to = take_command()
                send_email(to, "Subject", content)
                speak("Email has been sent.")
            except Exception as e:
                speak("Sorry, I am not able to send this email.")
        elif 'exit' in query:
            speak("Goodbye!")
            exit()
        else:
            speak("I am sorry, I don't understand.")

# End of program
