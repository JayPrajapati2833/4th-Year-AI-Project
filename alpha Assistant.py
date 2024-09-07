import pyttsx3
import speech_recognition as sr
import pyautogui
import requests 
import pywhatkit
import cv2
import PyPDF2
import pygame
import speedtest
import json
import pyjokes
import random
import platform
import psutil
import requests 
import os
import time
import datetime
import webbrowser
import wikipedia
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from tkinter import filedialog
from plyer import notification
import winsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)

def Speak(audio):
    print("       ")
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        Speak("Listening...")
        r.pause_threshold = 1

        try: 
            audio = r.listen(source)
            print("Recognizing.....")
            query = r.recognize_google(audio, language ='en')
            print(f"your command {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, please repeat?")
            return ""

def setAlaram(time):
    altime = str(datetime.datetime.now().strptime(time,"%I:%M %p"))
    altime = altime[11:-3]
    horeal = altime[:2]
    horeal = int(horeal)
    mireal = altime[3:5]
    mireal = int(mireal)
    print(f"Done, alaram set for{time}")
    while True:
        if horeal==datetime.datetime.now().hour:
            if mireal==datetime.datetime.now().minute:
                print("alaram is running") 
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif mireal<datetime.datetime.now().minute:
                break


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
    greetMe()
    try:
        while True:
            query = TakeCommand().lower()

            if 'exit alpha' in query or 'close alpha' in query or 'bye alpha' in query or 'stop alpha' in query:
                Speak("Closing alpha. Goodbye!")
                break 
            
            if 'alpha' in query or 'alfa' in query:
                if 'hello' in query:
                    Speak("hello sir. How may i help you.")

                #search on youube
                elif 'search on youtube' in query:
                    Speak("Ok sir, searching...")
                    query = query.replace("alpha", "")
                    query = query.replace("search on youtube", "")
                    web = "https://www.youtube.com/results?search_query=" + query
                    webbrowser.open(web)
                    Speak("Sir, here are the results")

                #wikipedia summary
                elif 'wikipedia summary' in query:
                    Speak("Searching on wikipedia....")
                    query = query.replace("alpha", "")
                    query = query.replace("wikipedia summary", "")
                    summary = wikipedia.summary(query, 3)
                    Speak(f"according to wikipedia {summary}")
                elif 'wikipedia' in query:
                    Speak("Searching on wikipedia....")
                    query = query.replace("alpha", "")
                    query = query.replace("wikipedia", "")
                    summary = wikipedia.summary(query)
                    Speak(f"according to wikipedia {summary}")
                
                # Screenshot
                elif "take screenshot" in query:
                    Speak('tell me a name for the file')
                    name = TakeCommand().lower()
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    Speak("screenshot saved")

                # IP address found
                elif "what is my ip address" in query:
                    Speak("Checking")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        Speak(f"your ip adress is {ipAdd}")
                        # Speak(ipAdd)
                    except Exception as e:
                        Speak("network is weak, please try again some time later")

                # Volume up
                elif "volume up" in query:
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    
                # Volume down
                elif "volume down" in query:
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")

                # mute
                elif "mute" in query:
                    pyautogui.press("volumemute")
                
                # Notepad open 
                elif "open notepad and write your name" in query:
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.write('notepad')
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.write("Alpha")
                
                # Notepad close
                elif "close notepad" in query:
                    os.system("taskkill /f /im notepad.exe")
        
                
                        
                #  close softwares vs code, visual studio, photoshop, excel, word, cmd
                elif 'close ' in query:
                    Speak('Ok sir closing...')
                    if 'vs code' in query:
                        pyautogui.hotkey('alt', 'f')
                        time.sleep(1)
                        pyautogui.press('x')

                    elif 'excel' in query:
                        os.system("TASKKILL /f /im EXCEL.EXE")
                    elif 'word' in query:
                        os.system("TASKKILL /f /im WINWORD.EXE")
                    elif 'powerpoint' in query:
                        os.system("TASKKILL /f /im POWERPNT.EXE")
                    elif 'this pc' in query:
                        pyautogui.hotkey('ctrl', 'w')
                    elif 'cmd' in query:
                        os.system("taskkill /f /im cmd.exe")
                    elif "paint" in query:
                        print('close paint')
                        os.system("TASKKILL /f /im MSPAINT.EXE")
                    elif "window" in query:
                        print('window closing')
                        pyautogui.hotkey('alt','f4')

                elif " draw rectangle" in query:
                    pyautogui.moveTo(515, 75, 1)
                    pyautogui.rightClick()
                    pyautogui.click()
                    pyautogui.moveTo(965, 273, 1)
                    pyautogui.dragRel(700, 300, 1)
                
                elif " draw rectangular spiral" in query:
                    pyautogui.moveTo(100, 193, 1)
                    pyautogui.rightClick()
                    pyautogui.click()
                    distance = 300
                    while distance > 0:
                        pyautogui.dragRel(distance, 0, 0.1, button="left")
                        distance = distance - 10
                        pyautogui.dragRel(0, distance, 0.1, button="left")
                        pyautogui.dragRel(-distance, 0, 0.1, button="left")
                        distance = distance - 10
                        pyautogui.dragRel(0, -distance, 0.1, button="left")

                elif "drag yash" in query:
                    pyautogui.moveTo(346, 55, 2)
                    pyautogui.dragRel(1634, 41, 2)

                elif 'tell me a joke' in query:
                    Speak(pyjokes.get_joke())

                elif 'system information' in query or 'hardware information' in query:
                    system_info = f"System: {platform.system()} {platform.version()}\n"
                    system_info += f"Processor: {platform.processor()}\n"
                    system_info += f"Architecture: {platform.architecture()}\n"
                    system_info += f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
                    system_info += f"CPU Cores: {psutil.cpu_count(logical=False)}\n"
                    system_info += f"CPU Threads: {psutil.cpu_count(logical=True)}\n"
                    print(system_info)
                    Speak("Here is your system information.")
                    Speak(system_info)
                    
                elif 'find my location' in query:
                    ipAdd = requests.get('https://api.ipify.org').text
                    response = requests.get(f"https://ipinfo.io/{ipAdd}/json")
                    data = response.json()
                    Speak(f'IP Address:{data.get("ip")}')
                    Speak(f'Location: {data.get("city")}')
                    Speak(f'Region: {data.get("region")}')
                    Speak(f'Country: {data.get("country")}')
                    Speak(f'Location Coordinates: {data.get("loc")}')

                elif 'weather' in query:
                    url = f'https://www.google.com/search?q=weather+{"Ahmedabad"}'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # Extracting temperature and description
                    temperature = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
                    description = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text
                    Speak(f"Weather in Ahmedabad: {temperature}, {description}")

                elif "how" in query:
                    query = query.replace("alpha", "")
                    max_result = 1
                    question_to = search_wikihow(query, max_result)
                    assert len(question_to) == 1
                    question_to[0].print()
                    Speak(question_to[0].summary)

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

                # elif "speed test" in query:
                #     st = speedtest.Speedtest()
                #     download_speed = st.download() / 1000000  # Convert to Mbps
                #     upload_speed = st.upload() / 1000000  # Convert to Mbps
                #     Speak(f"Sir, we have {download_speed:.2f} Mbps download speed and {upload_speed:.2f} Mbps upload speed.")

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

                elif "shutdown the system" in query:
                    os.system("shutdown /s /t 5")
                
                elif "restart the system" in query:
                    os.system("shutdown /r /t 5")
                    
                elif "sleep the system" in query:
                    print("sleeping")
                    pyautogui.hotkey('win','x')
                    time.sleep(1)
                    pyautogui.press('u')
                    time.sleep(1)
                    pyautogui.press('s')

                elif 'read pdf' in query:
                    path = filedialog.askopenfilename()
                    pdf = open(path,'rb')
                    pdfread = PyPDF2.PdfReader(pdf)
                    pages = len(pdfread.pages)

                    Speak(f"Total pages in pdf are {pages}")
                    print(f"Total pages in pdf are {pages}")
                    Speak("Enter page number which i have to read")
                    pag = int(input("Enter page number : "))
                    pag = max(0, min(pag, pages - 1))
                    pg = pdfread.pages[pag]
                    text = pg.extract_text()
                    Speak(text)
                
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
                        file.write(f"{tasks[i]}\n")
                        file.close()

                elif "tell my schedule" in query:
                    if os.path.exists("tasks.txt"):
                        print('your schedule')
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                            )
                    else:
                        print("No schedule found.")

                elif "clear my schedule" in query:
                    file = open("tasks.txt","w")
                    file.write(f"")
                    file.close()
                    Speak("Schedule is deleted")

                elif 'set alarm' in query:
                    Speak("Tell me time for alaram like set alaram to 5:30 am")
                    alaram = TakeCommand()  #set alaram to 5:30 am
                    alaram = alaram.replace("set alaram to","")
                    alaram = alaram.replace(".","")
                    alaram = alaram.upper()
                    setAlaram(alaram)

                elif 'play jailer movie' in query:
                    # npath = "D:\Movies\Jailer"
                    os.startfile("D:\\Movies\\Jailer.mkv")
                
                elif 'play music' in query:
                    # music_dir = 'E:\Musics'
                    songs = os.listdir("D:\\Music")
                    os.startfile(os.path.join("D:\\Music", random.choice(songs)))

                # chrome
                # Whastsapp message send
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

                # Google search
                elif 'google search' in query:
                    query = query.replace("alpha", "")
                    query = query.replace("google search", "")
                    pyautogui.hotkey('alt', 'd')
                    pyautogui.write(f"{query}", 0.1)
                    pyautogui.press('enter')

                # Open website
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
            
                elif 'open new window' in query:
                    pyautogui.hotkey('ctrl', 'n')
                
                elif 'open new tab' in query:
                    pyautogui.hotkey('ctrl', 't')

                elif 'maximize this window' in query:
                    pyautogui.hotkey('alt', 'space')
                    time.sleep(1)
                    pyautogui.press('x')

                elif ' open incognito window' in query:
                    pyautogui.hotkey('ctrl','shift','n')

                elif 'open history' in query:
                    pyautogui.hotkey('ctrl', 'h')
                
                elif 'open downloads' in query:
                    pyautogui.hotkey('ctrl', 'j')
                
                elif 'previous tab' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')
            
                elif 'next tab' in query:
                    pyautogui.hotkey('ctrl', 'tab')
        
                elif 'close tab' in query:
                    pyautogui.hotkey('ctrl', 'w')

                elif 'close chrome' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'w')

                # open softwares - vs code, visual studio, photoshop, excel, word, cmd
                elif 'open' in query:
                    Speak('Ok sir opening...')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    query = query.replace("alpha", "")
                    query = query.replace("open", "")
                    pyautogui.write(query)
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(1)    



                elif "who are you" in query:
                    # print('My Name Is Alpha')
                    Speak('My Name Is Alpha')
                    Speak('I can Do Everything that my creator programmed me to do')
                
                elif "who created you" in query:
                    Speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
    except Exception as e:
        print(f"Error: {e}")    