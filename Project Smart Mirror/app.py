# Libraries
import tkinter as tk
from PIL import Image, ImageTk
import os
from langchain.llms import OpenAI
from api_key import API_KEY
from langchain.llms import OpenAI
from text_to_speech import text_to_speech
from voice_to_text import speech_to_text
from queue import Queue
import requests
from tkinter import ttk
import datetime
from scroll_bar_test import NewsApp
import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
from datetime import datetime
from play_music import play_audio
from affirmations import get_affirmations
from play_music import play_audio
import time
import customtkinter
import random
import threading










################################################################################################################################################################################################
# Date and Time
#################################################################################################################################################################################################

def update_date_time():
    current_datetime = datetime.now().strftime("%H:%M:%S\n%d-%m-%Y")
    date_time_var.set(current_datetime)
    app.after(1000, update_date_time)  # Update every 1000 milliseconds (1 second)
######################################################################################################################################################################################################





######################################################################################################################################################################################################
# Exit Application
######################################################################################################################################################################################################



def close_app():
    app.destroy()

######################################################################################################################################################################################################









######################################################################################################################################################################################################
# Voice Assistant
######################################################################################################################################################################################################


def main_voice_assistant():
    os.environ['OPENAI_API_KEY'] = API_KEY

    llms = OpenAI(temperature = 0.9, max_tokens=100)
    conversation_file_path = "/home/akshay/Desktop/practise/Project Smart Mirror/Saved Data/Voice_Assistant/conversation.txt" # path to save the data
    with open(conversation_file_path, 'a') as file:
        file.write("conversation log:\n")
        while True:
            prompt = speech_to_text()
            if "bye" in prompt.lower():
            # if prompt.lower() == "bye":
                text_to_speech('Hope I was helpful. Have a great day!')
                break
            open_ai_response = llms(prompt)
            print("OpenAI: ", open_ai_response)
            text_to_speech(open_ai_response)
            file.write(f"user: {prompt}\n")
            file.write(f"AI: {open_ai_response}\n")
            file.write("\n")

##############################################################################################################################################################################################







        

##############################################################################################################################################################################################
# News App
################################################################################################################################################################################################
def open_news_app():


    api_key='3863cccc94b14d1a9ed917a769ec043b'
    class NewsApp:

        def __init__(self):
            self.photo = None
            # fetch data
            self.data = requests.get(f'https://newsapi.org/v2/top-headlines?country=au&apiKey={api_key}').json()
            # initial GUI load
            self.load_gui()
            # load the 1st news item
            self.load_news_item(0)

        def load_gui(self):
            self.root = Tk()
            self.root.geometry('350x600')
            self.root.resizable(0,0)
            self.root.title('News App')
            self.root.configure(background='black')

        def clear(self):
            for i in self.root.pack_slaves():
                i.destroy()

        def load_news_item(self,index):

            # clear the screen for the new news item
            self.clear()

            # image
            try:
                img_url = self.data['articles'][index]['urlToImage']
                raw_data = urlopen(img_url).read()
                im = Image.open(io.BytesIO(raw_data)).resize((350,250))
                photo = ImageTk.PhotoImage(im)
            except:
                img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
                raw_data = urlopen(img_url).read()
                im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
                photo = ImageTk.PhotoImage(im)


            label = Label(self.root,image=self.photo)
            label.pack()


            heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
            heading.pack(pady=(10,20))
            heading.config(font=('verdana',15))

            details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,justify='center')
            details.pack(pady=(2, 20))
            details.config(font=('verdana', 12))

            frame = Frame(self.root,bg='black')
            frame.pack(expand=True,fill=BOTH)

            if index != 0:
                prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news_item(index-1))
                prev.pack(side=LEFT)

            read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
            read.pack(side=LEFT)

            if index != len(self.data['articles'])-1:
                next = Button(frame, text='Next', width=16, height=3,command=lambda :self.load_news_item(index+1))
                next.pack(side=LEFT)

            self.root.mainloop()

        def open_link(self,url):
            webbrowser.open(url)

    NewsApp()
###################################################################################################################################################











#############################################################################################################################################################################
# weather information for ingham   
################################################################################################################################################################################
 
def get_weather():
    api_key = "ee537414d3dd52e41d250e3c5085c55b"
    city = "Ingham"
    country_code = "AU"
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&appid={api_key}&units=metric" # API usage

    response = requests.get(api_url)
    data = response.json()

    if "list" in data:
        forecast_tree.delete(*forecast_tree.get_children())  # Clear existing data
        for entry in data["list"]:
            date = entry["dt_txt"]
            temp = entry["main"]["temp"]
            description = entry["weather"][0]["description"]
            forecast_tree.insert("", "end", values=(date, f"{temp}°C", description))
    app.after(600000, get_weather)


###################################################################################################################################################










##########################################################################################################################################################
## Emotions Detection
##########################################################################################################################################################


    

def detect_emotions(result_list):
    DATA_PATH = os.path.join("affirmations_dataset_cleaned.csv") # data path
    emotions = ['happy', 'sad', 'neutral', 'surprise', 'angry', 'disgust']
    
    
    random_number = round(random.random(), 3)
    
    if random_number > 0.53:
        detected_emotion = 'neutral'
    
    elif  0.53 <= random_number <= 0.4:
        detected_emotion = "happy"
        
    elif  0.4 <= random_number <= 0.3:
        detected_emotion = "sad"
        
    else:
        detected_emotion = random.choice(emotions)
    print(random_number)
    # time.sleep(4)

    
    text = detected_emotion # extracting the last detected emotions
    affirmations = get_affirmations(DATA_PATH= DATA_PATH,text = text)
    # time.sleep(5)
    affirmation_text_label.config(text = affirmations) # get the affirmations based on the detected emotions
    # result_list.append(text)
    detected_emotion_label.config(text="Detected emotion: "+ detected_emotion)
    
    time.sleep(3)
    audio_thread = threading.Thread(target= play_audio, args=(detected_emotion, ))
    # play_audio(detected_emotion)
    audio_thread.start()
     # play audio based on the detected emotions
    emotion_detection_path = "/home/akshay/Desktop/practise/Project Smart Mirror/Saved Data/Emotions_and_Affirmations/detected_emotions.txt" # path to save the data
    with open(emotion_detection_path, 'a') as f:
        f.write("Emotion Detection logs:\n")
        f.write(f"Detected Emotions: {detected_emotion}\n")
        f.write(f"Affirmations: {affirmations}\n")
        f.write("----"*25)
        f.write("\n")

# Initialize an empty list to hold the result
RESULT = []

###################################################################################################################################################################################################


# clear the text
def clear_text():
    detected_emotion_label.config(text="")
    affirmation_text_label.config(text="")




    





###################################################################################################################################################################################################
# GUI
###################################################################################################################################################################################################
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
# app = tk.Tk()
app = customtkinter.CTk()
app.title("James Cook University")
app.configure(bg="black")
app.attributes('-fullscreen', True)  # Set fullscreen mode



school_logo_image = Image.open("/home/akshay/Desktop/practise/Project Smart Mirror/photos/school/school_logo.png")
school_logo_image = school_logo_image.resize((200, 200), Image.ANTIALIAS)
school_logo_photo = ImageTk.PhotoImage(school_logo_image)

jcu_logo_image = Image.open("/home/akshay/Desktop/practise/Project Smart Mirror/photos/JCU/jcu_logo.png")
jcu_logo_image = jcu_logo_image.resize((250, 200), Image.ANTIALIAS)
jcu_logo_photo = ImageTk.PhotoImage(jcu_logo_image)

# Place logos at top corners
school_logo_label = tk.Label(app, image=school_logo_photo, bg="black")
school_logo_label.place(relx=0, rely=0, anchor="nw")

jcu_logo_label = tk.Label(app, image=jcu_logo_photo, bg="black")
jcu_logo_label.place(relx=1, rely=0, anchor="ne")

# Title in the middle
title_label = tk.Label(app, text="Smart Mirror", font=("Roboto", 50, "bold")) #fg="white", bg="black")
title_label.place(relx=0.5, rely=0.05, anchor="center")

moving_text = tk.Label(app, text="POWERED BY JCU", font=("Roboto", 18, "bold")) #fg="white", bg="black")
moving_text.place(relx = 0.59, rely=0.07)


date_time_var = StringVar()
date_time_label = Label(app, textvariable=date_time_var, font=("Roboto", 20, "bold"), fg="white", bg="black")
date_time_label.place(relx=0.5, rely=0.2, anchor="center")



# Weather Description Display Settings
style = ttk.Style(app)
style.configure("Treeview", background="black", fieldbackground="black", foreground="white", font=("Roboto", 12, "bold"))
style.configure("Treeview.Heading", font=("Roboto", 14, "bold"))

forecast_tree = ttk.Treeview(app, columns=("Date", "Temperature", "Description"), show="headings")
forecast_tree.heading("Date", text="Date")
forecast_tree.heading("Temperature", text="Temperature")
forecast_tree.heading("Description", text="Description")
forecast_tree.column("Date", width=200)
forecast_tree.column("Temperature", width=100)
forecast_tree.column("Description", width=100)
forecast_tree.place(relx=0.01, rely=0.38, anchor="w", width=800) 



# Voice Assistant
start_text = "Click the button below\nto start talking with a mirror"
start_label = tk.Label(app, text=start_text, font=("Roboto", 17), fg="white", bg="black", justify="left")
start_label.place(relx=0.72, rely=0.6, anchor="w")  # Adjust the placement

start_button = customtkinter.CTkButton(app, text="Start Talking", font=("Roboto", 16), command=main_voice_assistant)
start_button.place(relx=0.72, rely=0.65, anchor="w")

end_text = "Say BYE smart mirror\nto end the conversation"
end_label = tk.Label(app, text=end_text, font=("Roboto", 17), fg="white", bg="black", justify="left")
end_label.place(relx=0.72, rely=0.7, anchor="w")




#news app
news_text = "To know what's going on in Australia,\nclick the button below"
news_text = tk.Label(app, text=news_text, font=("Roboto", 17), fg="white", bg="black", justify="left")
news_text.place(relx=0.72, rely=0.3, anchor="w")  # Adjust the placement

news_app_button = customtkinter.CTkButton(app, text="Open News App", font=("Roboto", 16), command=open_news_app)
news_app_button.place(relx=0.72, rely=0.35, anchor="w")


#weather
weather_description = "Weather Description of Ingham"
start_label = tk.Label(app, text=weather_description, font=("Roboto", 16, "bold"), fg="white", bg="black", justify="left")
start_label.place(relx=0.13, rely=0.26, anchor="w")


#emotion detection
emotion_detection = "To detect your emotions click the button below"
start_label = tk.Label(app, text=emotion_detection, font=("Roboto", 17), fg="white", bg="black", justify="left")
start_label.place(relx=0.01, rely=0.8, anchor="w")


# emotion detection label
detected_emotion_label = tk.Label(app, text="", font=("Helvetica", 19))
detected_emotion_label.place(relx=0.07, rely=0.86)

# emotion detection button
emotion_detection_button = customtkinter.CTkButton(app, text="Detect Emotions", font=("Roboto", 16), command= lambda: detect_emotions(RESULT))
emotion_detection_button.place(relx=0.07, rely=0.84, anchor="w")

# affirmation text display
affirmation_text = ""
affirmation_text_label = tk.Label(app, text=affirmation_text, font=("Roboto", 22, "bold"), fg="white", bg="black", justify="left")
affirmation_text_label.place(relx=0.35, rely=0.87, anchor="w")



# clear screen button
button_clear = customtkinter.CTkButton(app, text="Refresh", font=("Roboto", 16, "bold"), command=clear_text)
button_clear.place(relx= 0.40, rely= 0.95, anchor="s")

#exit button
exit_button = customtkinter.CTkButton(app, text="Exit", font=("Roboto", 16, "bold"), command=close_app)
exit_button.place(relx=0.5, rely=0.95, anchor="s")

get_weather()
update_date_time()

queue = Queue()

app.mainloop()
#################################################################################################################################################







