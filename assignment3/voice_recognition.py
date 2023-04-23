import pandas as pd
import speech_recognition as sr
import pyttsx3


class HandleDataset:
    def __init__(self,location):
        self.speaker = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.location = location
        self.df = pd.read_csv(self.location)
        self.speak("Your dataset is loaded...")
        

    def take_input(self):
        try:
            with sr.Microphone() as source:
                print("Preparing....")
                self.recognizer.adjust_for_ambient_noise(source,duration = 2)
                print("Listening...")
                self.audio = self.recognizer.listen(source)
                self.text = self.recognizer.recognize_google(self.audio)
                print(f"User Input : {self.text}")
        except:
            print("Speak Something..")
            self.speak("Speak something.")
            self.text = "none"


    def speak(self,text):
        self.speaker.say(text)
        self.speaker.runAndWait()


    def show_column_names(self):
        for i in self.df.columns:
            print(i)
            self.speak(i)
        print("-"*50)
    

    def show_null_values(self):
        print(self.df.isnull().sum())
        self.speak(self.df.isnull().sum())
        print("-"*50)


    def show_shape(self):
        print(self.df.shape)
        self.speak(f"Total Rows : {self.df.shape[0]} and Total Columns : {self.df.shape[1]}")
        print("-"*50)


    def show_head(self):
        print(self.df.head())
        print("-"*50)
               

    def main_controls(self):
        
        while True:
            self.take_input()
            if "column names" in self.text:
                self.show_column_names()
            elif "null value" in self.text:
                self.show_null_values()
            elif "shape" in self.text:
                self.show_shape()
            elif "glance" in self.text or "few rows" in self.text:
                self.show_head()
            elif "none" in self.text:
                pass
            elif "stop" in self.text:
                self.speak("Mission End...")
                break
            else:
                print("Please Say Again")
                self.speak("Please Say Again")



location = "C:\\Users\\VIMAL GRACE M\\OneDrive\\Desktop\\Naan Mudhalvan\\day 15\\diabetes.csv"
dataset = HandleDataset(location)
dataset.main_controls()



        
    





    




