import tkinter as tk
from PIL import Image, ImageTk
# from app_voice_assistant import main
import threading
import os
from langchain.llms import OpenAI
from api_key import API_KEY
from langchain.llms import OpenAI
from text_to_speech import text_to_speech
from voice_to_text import speech_to_text
from queue import Queue
import requests

def close_app():
    app.destroy()

def move_text():
    x_position = -100  # Start off the screen on the left
    animation = False
    while not animation:
        moving_text.place(x=x_position, y=200)
        app.update()
        x_position += 5  # Adjust the speed of movement
        if x_position > app.winfo_screenwidth():
            x_position = -200  # Reset the position once it goes off the screen
        app.after(50)   # Adjust the animation speed
        
# conversation_active = False    
def main_voice_assistant():
    os.environ['OPENAI_API_KEY'] = API_KEY

    llms = OpenAI(temperature = 0.9)
    # original_start_text = start_label.cget("text")
    conversation_event_end = threading.Event()
    while True:
        prompt = speech_to_text()
        if prompt.lower() == "bye":
            text_to_speech('Hope I was helpful. Have a great day!')
            break
        open_ai_response = llms(prompt)
        print("OpenAI: ", open_ai_response)
        text_to_speech(open_ai_response)
        # app.after(0, lambda: start_label.config(text=open_ai_response))  # Update the label with conversation info
    conversation_event_end.set()
    


    
    
    
    
    
def start_talking():
    start_label.config(text="You started talking with the mirror!")
    move_thread = threading.Thread(target=move_text)
    assistant_thread = threading.Thread(target=main_voice_assistant)
    
    move_thread.start()
    assistant_thread.start()
    
    app.after(0, lambda: start_label.config(text="You started talking with the mirror!"))
    app.after(main_voice_assistant, lambda: start_label.config(text="Say 'Hi Smart Mirror' \nto start talking with a mirror"))
    
    

    
def get_weather():
    api_key = "ee537414d3dd52e41d250e3c5085c55b"  # Replace with your actual API key
    city = "Cairns"
    country_code = "AU"
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&appid={api_key}&units=metric"

    response = requests.get(api_url)
    data = response.json()

    if "list" in data:
        forecast_text = "7-Day Weather Forecast:\n\n"
        for entry in data["list"]:
            date = entry["dt_txt"]
            temp = entry["main"]["temp"]
            description = entry["weather"][0]["description"]
            forecast_text += f"{date}:\nTemperature: {temp}°C\nDescription: {description}\n\n"
    else:
        forecast_text = "data not available"

    forecast_label.config(text=forecast_text)

app = tk.Tk()
app.title("James Cook University")
app.configure(bg="black")
app.attributes('-fullscreen', True)  # Set fullscreen mode

# Load and resize the logo image
logo_image = Image.open("jcu_logo.png")  # Replace with your logo image path
logo_image = logo_image.resize((250, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)

title_frame = tk.Frame(app, bg="black")
title_frame.pack(pady=50)

logo_label = tk.Label(title_frame, image=logo_photo, bg="black")
logo_label.pack(side="right")

title_label = tk.Label(title_frame, text="Powered By", font=("Roboto", 32), fg="white", bg="black")
title_label.pack(side="left", padx=10)

title_frame.pack()

moving_text = tk.Label(app, text="SMART MIRROR IS IN PROGRESS", font=("Roboto", 24), fg="white", bg="black")
moving_text.place(x=0, y=0)  # Initial position off the screen

exit_button = tk.Button(app, text="Exit", font=("Roboto", 16), command=close_app)
exit_button.place(relx=0.5, rely=0.9, anchor="s")
# forecast_label = tk.Label(app, text="7-Day Weather Forecast:", font=("Arial", 24), fg="white", bg="black")
# forecast_label.place(relx=0.05, rely=0.6, anchor="w")  # Adjust the placement

# Display dummy forecast
dummy_forecast = [
    {"date": "2023-08-11", "temp": 25, "description": "Sunny"},
    {"date": "2023-08-12", "temp": 24, "description": "Partly Cloudy"},
    {"date": "2023-08-13", "temp": 22, "description": "Cloudy"},
    {"date": "2023-08-14", "temp": 23, "description": "Showers"},
    {"date": "2023-08-15", "temp": 20, "description": "Rain"},
    {"date": "2023-08-16", "temp": 22, "description": "Cloudy"},
    {"date": "2023-08-17", "temp": 26, "description": "Sunny"},
]


forecast_text = "Dummy Forecast:\n\n"
for day in dummy_forecast:
    forecast_text += f"{day['date']}:\nTemperature: {day['temp']}°C\nDescription: {day['description']}\n\n"

dummy_forecast_label = tk.Label(app, text=forecast_text, font=("Arial", 16), fg="white", bg="black", justify="left")
dummy_forecast_label.place(relx=0.05, rely=0.5, anchor="w")  # Adjust the placement

start_text = "Say 'Hi Smart Mirror' \nto start talking with a mirror"
start_label = tk.Label(app, text=start_text, font=("Arial", 16), fg="white", bg="black", justify="left")
start_label.place(relx=0.72, rely=0.6, anchor="w")  # Adjust the placement

start_button = tk.Button(app, text="Start Talking", font=("Arial", 16), command=start_talking)
start_button.place(relx=0.72, rely=0.55, anchor="w")

forecast_label = tk.Label(app, text="", font=("Arial", 12), wraplength=400, justify="left")
forecast_label.pack(padx=20, pady=20)

# Fetch weather data and update the label
get_weather()

# main()
  # Start the continuous moving text animation
# stop_animation = False  # To control the animation loop
# animation_thread = threading.Thread(target=move_text)  # Create a thread for animation
# animation_thread.start()  # Start the animation thread

animation = True
animation_thread = threading.Thread(target=move_text)  # Create a thread for animation
animation_thread.start()
move_text()
queue = Queue()
# app.after(100, check_queue)  # Start checking the queue for updates
# app.mainloop()
app.mainloop()


# stop_animation = True






