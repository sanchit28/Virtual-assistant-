import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import shutil
import time


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 
engine.setProperty('rate', 150)
print(type(engine))
print(engine)


def speak(audio): #to speak, Text to Speech
    engine.say(audio)
    engine.runAndWait()


def tellDay(): # This function is for telling the day of the week 
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number  
    # that will help us in telling the day 
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week) 

def wishMe():
    hour=int(datetime.datetime.now().hour)
    # minute= int(datetime.datetime.now().minute)
    time_now = time.strftime("%H:%M:%p")
    if (hour>=0 and hour<12):
        speak(f"Good Morning Boss!, its {time_now}")     #Text to Speech
    elif(hour>=12 and hour<18):
        speak(f"Good Afternoon Boss, its {time_now}")
    else:
        speak(f"Good Evening Boss, its {time_now}")
    speak("I am Steffi, Your Virtual Assistant ")

def usrname(): 
	speak("What should i call you sir") 
	uname = takeCommand() 
	speak("Welcome Mister") 
	speak(uname) 
    
	columns = shutil.get_terminal_size().columns 
    

def takeCommand(): #it takes microphone input from the user and return the string output
     r=sr.Recognizer()    #recogniser class helps in recognising the audio
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1 #it refers to the amount of time gap after which the audio is supposed to be complete
         r.energy_threshold =300
         audio=r.listen(source) #digitaldata of whatsoever hs been spoken will be stored in audio
     try:
      print("Recognising...")
      query=r.recognize_google(audio,language="en-in")
      print(f"User said: {query}\n")

     except Exception as e:
      print(e)   
      print("Say that again please!")
      #speak("Say that again please!")
      return "None"
     return query


if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	wishMe() 
	usrname() 


while True:
#if 1:
    query = takeCommand().lower()
    #logic for executing tasks based on query
    if 'wikipedia' in query:   #wikipedia is a keyword. If user doesnt say that, it will not work.
        speak("Searching Wikipedia")
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open facebook' in query:
        webbrowser.open("fb.com")

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'google' in query:
        query=query.replace("google","")
        query=query.replace("search","")
        webbrowser.open("https://google.com/search?q=%s" % query)

    elif (('music' in query) or ("song" in query)):
         # music_dir = "G:\\Song"
        #music_dir= 'D:\\OldSongs' #\\ slash is to escape the character
        music_dir = 'D:\\volume E\\MUSIC 3.O\\BOLLYWOOD'
        songs = os.listdir(music_dir)  #listdir is used to enlist all the songs of mentioned directory
        #print(songs)
        
        os.startfile(os.path.join(music_dir,songs[0])) #song[0] will play the first song. using random module, song can be shuffled

    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M%S")
        speak("Sir, the time is")
        speak(time)
        print(time)

    elif 'how are you' in query:
        speak("I am fine, thank you")
        speak("how are you, sir")

    elif 'fine' in query in query or 'I am good' in query:
        speak("it's good to know, sir")

    elif 'who created you' in query:
        speak("I have been created by Utkarsh")

    elif "which day it is" in query: 
        tellDay()

    elif 'open notepad' in query:
        # path = " enter notepad path"
        path = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(path)

    elif 'tell me a joke' in query:
        speak(pyjokes.get_joke())

    elif 'open command prompt' in query:
        os.system("start cmd")


    elif "time to sleep" in query or "stop listening" in query or "no thanks" in query:
        speak("Thanks for using me sir, Have a good day")
        #subprocess.call("shutdown / h")
        exit()
        
    speak("sir, do you have any other work!")
     