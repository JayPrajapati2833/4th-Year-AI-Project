import pyttsx3
import speech_recognition as sr
import time
import datetime
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import os
import pyaudio
from plyer import notification
from pygame import mixer
from pywikihow import search_wikihow
import psutil
import speedtest
import json
import requests
import PyPDF2
from tkinter import filedialog

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate', 190)


def Speak(audio):
    print("       ")
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:    
            audio = r.listen(source)
            print("Recognizing.....")
            query = r.recognize_google(audio, language ='en')
            print(f"your command {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said. Could you please repeat?")
            return ""

def greetMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if (hour > 6 and hour < 12):
        Speak("Good Morning sir")
    elif (hour >= 12 and hour < 16):
        Speak("Good Afternoon sir")
    elif (hour >= 16 and hour < 19):
        Speak("Good evening sir")
    Speak(f"Time is {hour} Hour and {minute} minute")
    Speak("I am alpha. How my i help you")


if __name__ == "__main__":
    # greetMe()
    while True:
        query = TakeCommand().lower()
        if 'alpha' in query or 'alfa' in query:
            if 'hello' in query:
                Speak("hello sir. How may i help you.")

# *search on youtube any topic
            elif 'search on youtube' in query:
                Speak("Ok sir, searching...")
                query = query.replace("alpha", "")
                query = query.replace("search on youtube", "")
                web = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(web)
                Speak("Sir, here are the results")

# *summary of wikipedia
            elif 'wikipedia summary' in query:
                Speak("Searching on wikipedia....")
                query = query.replace("alpha", "")
                query = query.replace("wikipedia summary", "")
                summary = wikipedia.summary(query, 3)
                Speak(f"according to wikipedia {summary}")

# *wikipedia on any topic
            elif 'wikipedia' in query:
                Speak("Searching on wikipedia....")
                query = query.replace("alpha", "")
                query = query.replace("wikipedia", "")
                summary = wikipedia.summary(query)
                Speak(f"according to wikipedia {summary}")

#   * search on google
            elif 'search' in query:
                Speak('Ok sir, searching...')
                query = query.replace("alpha", "")
                query = query.replace("search", "")
                pywhatkit.search(query)
                Speak("sir here is the result")
                
# * open wqebsite like stackoverflow
            elif 'open website' in query:
                Speak("Ok sir, opening.....")
                query = query.replace("alpha", "")
                query = query.replace("open website", "")
                query = query.replace(" ", "")
                website = 'https://' + query + '.com/'
                # 'https://stackoverflow.com/'
                print(website)
                webbrowser.open(website)
                Speak("sir " + query + " website opened")
                
                
#! new add this 
# *send whats app message
            elif 'send whatsapp message' in query:
                Speak("what is the message")
                message = TakeCommand()
                webbrowser.open('https://web.whatsapp.com/')
                time.sleep(17)
                pyautogui.click(325, 270)
                query = query.replace("alpha", "")
                query = query.replace("send whatsapp message", "")
                print(query)
                pyautogui.typewrite(query)
                time.sleep(5)
                pyautogui.click(294, 430)
                time.sleep(3)
                pyautogui.click(896, 972)
                pyautogui.typewrite(message)
                time.sleep(3)
                pyautogui.click(1845, 970)
            
# *Take screenshot with file name
            elif 'take screenshot' in query:
                s = pyautogui.screenshot()
                Speak("Screenshot Name")
                sname = TakeCommand()
                s.save(
                    f'C:\\Users\\Jaimin\\OneDrive\\Pictures\\Screenshots\\' + sname + '.jpg')                    
                
#! Open softwares
           
#    * open softwares - vs code, visual studio, photoshop, excel, word, cmd
            elif 'open' in query:
                Speak('Ok sir opening...')
                if 'vs code' in query:
                    os.startfile(
                        "C:\\Users\\Jaimin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                elif 'visual studio' in query:
                    os.startfile(
                        "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe")
                elif 'excel' in query:
                    os.startfile(
                        "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                elif 'word' in query:
                    os.startfile(
                        "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                elif 'powerpoint' in query:
                    os.startfile(
                        "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                elif 'photoshop' in query:
                    os.startfile(
                        "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe")
                elif 'cmd' in query:
                    os.system("start cmd")
                elif 'chrome' in query:
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    
# * close softwares vs code, visual studio, photoshop, excel, word, cmd
            elif 'close ' in query:
                Speak('Ok sir closing...')
                if 'visual studio' in query:
                    os.system("TASKKILL /f /im devenv.exe")
                elif 'excel' in query:
                    os.system("TASKKILL /f /im EXCEL.EXE")
                elif 'word' in query:
                    os.system("TASKKILL /f /im WINWORD.EXE")
                elif 'powerpoint' in query:
                    os.system("TASKKILL /f /im POWERPNT.EXE")
                elif 'photoshop' in query:
                    os.system("TASKKILL /f /im Photoshop.exe")
                    

# * schedule my day todos
            elif "schedule my day" in query:
                tasks = [] #Empty list 
                file = open("tasks.txt","a")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    Speak(f"Enter task {i+1}")
                    task = TakeCommand().lower()
                    tasks.append(task)
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()

            elif "show my schedule" in query:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                    )

            elif "clear my schedule" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                Speak("Schedule is deleted")

            elif "how" in query:
                query = query.replace("alpha", "")
                max_result = 1
                question_to = search_wikihow(query, max_result)
                assert len(question_to) == 1
                question_to[0].print()
                Speak(question_to[0].summary)

            elif 'set alarm' in query:
                Speak("Specify the alarm time (HH:MM AM/PM): ")
                alarm_time = TakeCommand(); 
                try:
                    alarm_time_obj = datetime.datetime.strptime(alarm_time, '%I:%M %p')
                    print(f"Alarm set for {alarm_time_obj.strftime('%I:%M %p')}")
                    while True:
                        current_time = datetime.datetime.now().strftime('%I:%M %p')
                        if current_time == alarm_time:
                            print("Time's up! Wake up!")
                            # Replace the file path with the location of your music file
                            playsound('path_to_your_audio_file.mp3')
                            break
                except ValueError:
                    print("Invalid time format. Please enter the time in HH:MM AM/PM format.")
            
            elif 'battery' in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                pluged_on = battery.power_plugged
                other = battery.secsleft
                Speak(f"sir our battery percentage is {percentage} and plug is {pluged_on} ")

            elif 'switch the window' in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "speed test" in query:
                st = speedtest.Speedtest()
                download_speed = st.download() / 1000000  # Convert to Mbps
                upload_speed = st.upload() / 1000000  # Convert to Mbps
                Speak(f"Sir, we have {download_speed:.2f} Mbps download speed and {upload_speed:.2f} Mbps upload speed.")

            elif "tell me news" in query:
                Speak("Which topic you want news")
                topic = TakeCommand()
                Speak("please wait sir , fetching the latest news")
                main_url = f"https://newsapi.org/v2/top-headlines?country=in&category={topic}&apiKey=a15361ac0fab426aaa15b9275e75468a"
                main_page = requests.get(main_url).json()
                articles = main_page['articles']
                head = []
                numberByNews = ["First","Second","third","fourth","fifth"]
                for ar in articles:
                    head.append(ar["title"])
                for i in range(len(numberByNews)):
                    Speak(f"todays {numberByNews[i]} news is : {head[i]}")


# API_KEY = a15361ac0fab426aaa15b9275e75468a

            elif 'read pdf' in query:
                path = filedialog.askopenfilename()
                pdf = open(path,'rb')
                pdfread = PyPDF2.PdfFileReader(pdf)
                pages = pdfread.numPages
                Speak(f"Total pages in pdf are {pages}")
                print(f"Total pages in pdf are {pages}")
                Speak("Enter page number which i have to read")
                pag = int(input("Enter page number : "))
                pg = pdfread.getPage(pag) 
                text = pg.extractText()
                Speak(text) 