# from newsapi import NewsApiClient
# import pycountry
 
# # you have to get your api key from newapi.com and then paste it below
# newsapi = NewsApiClient(api_key='3863cccc94b14d1a9ed917a769ec043b')
 
# # now we will take name of country from user as input
# input_country = "Australia"
# input_countries = [f'{input_country.strip()}']
# countries = {}
 
# # iterate over all the countries in
# # the world using pycountry module
# for country in pycountry.countries:
 
#     # and store the unique code of each country
#     # in the dictionary along with it's full name
#     countries[country.name] = country.alpha_2
 
# # now we will check that the entered country name is
# # valid or invalid using the unique code
# codes = [countries.get(country.title(), 'Unknown code')
#          for country in input_countries]
 
# # now we have to display all the categories from which user will
# # decide and enter the name of that category
# option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
 
# # now we will fetch the new according to the choice of the user
# top_headlines = newsapi.get_top_headlines(
 
#     # getting top headlines from all the news channels
#     category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')
 
#   # fetch the top news under that category
# Headlines = top_headlines['articles']
 
#    # now we will display the that news with a good readability for user
# if Headlines:
#     for articles in Headlines:
#         b = articles['title'][::-1].index("-")
#         if "news" in (articles['title'][-b+1:]).lower():
#             print(
#                 f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
#         else:
#             print(
#                 f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
# else:
#     print(
#         f"Sorry no articles found for {input_country}, Something Wrong!!!")
# option = input("Do you want to search again[Yes/No]?")
# # if option.lower() == 'yes':
# #     continue
# # else:
# #         exit()


# import tkinter as tk

# def open_new_window():
#     new_window = tk.Toplevel(app)  # Create a new top-level window
#     new_window.title("New Window")  # Set the title of the new window
#     new_label = tk.Label(new_window, text="This is a new window!")  # Add a label to the new window
#     new_label.pack()

# app = tk.Tk()
# app.title("Main Window")

# open_button = tk.Button(app, text="Open New Window", command=open_new_window)
# open_button.pack()

# app.mainloop()
import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

api_key='3863cccc94b14d1a9ed917a769ec043b'
class NewsApp:

    def __init__(self, parent):
        self.photo = None
        self.parent = parent
        self.root = Toplevel(self.parent)
        # ... (rest of your NewsApp code)
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)
        # fetch data
        self.data = requests.get(f'https://newsapi.org/v2/top-headlines?country=au&apiKey={api_key}').json()
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(0)
        
    def on_window_close(self):
        self.parent.news_app = None  # Clear the reference to NewsApp
        self.root.destroy()
       

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('Mera News App')
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


        label = Label(self.root,image=photo)
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


# obj = NewsApp()