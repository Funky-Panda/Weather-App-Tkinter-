import tkinter as tk
from tkinter.constants import CENTER
from tkinter import font
import requests
from tkinter import messagebox


def test_function(entry):
    print('this is the entry',entry)

WIDTH = 600
HEIGHT = 500

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# f831ea411b2ed1667ff737debbebd382

def format_responce(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['main']
        Temperature=int(weather['main']['temp'])
        Feels_Like=int(weather['main']['feels_like'])

        final_str= 'City: %s \nConditions: %s  \nTemperature (°C) %s \nFeels Like(°C) : %s' % (name, desc,Temperature,Feels_Like) 

    except:   
        final_str = ('There was a problem \r retrieving \r that information')
    
    return final_str 


def get_weather(city):
    weather_key='f831ea411b2ed1667ff737debbebd382'
    url= 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response=requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_responce(weather)


root = tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='C:\\Users\\sulta\\Desktop\\Screenshot 2021-06-05 100409.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#398971',bd=5)
frame.place(relx=0.5,rely=0.1, relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame, font=40,bg='#b6e3d9')
entry.place(relx=0,rely=0,relwidth=0.65,relheight=1)

button = tk.Button(frame, text='Get Weather',font=40,bg='#4ad9b7',fg='dark blue', command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)


lower_frame=tk.Frame(root, bg='#398971', bd=10,)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame,font=('Garamond',35,'bold'),fg='black',bg='#b6e3d9')
label.place(relwidth=1,relheight=1)

print(tk.font.families())

root.mainloop()