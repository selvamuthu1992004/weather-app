import tkinter as tk
from tkinter import ttk
import requests

# Replace with your OpenWeatherMap API key
API_KEY = '0f78f1068de13f7cea546a2c7801bd36'

def get_weather(city, units):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return temperature, humidity, wind_speed
    else:
        return None, None, None

def show_weather():
    city = city_entry.get()
    units = units_var.get()
    units = 'metric' if units == 'Celsius' else 'imperial'
    
    temperature, humidity, wind_speed = get_weather(city, units)
    
    if temperature is not None:
        temperature_label.config(text=f'Temperature: {temperature}°')
        humidity_label.config(text=f'Humidity: {humidity}%')
        wind_speed_label.config(text=f'Wind Speed: {wind_speed} m/s' if units == 'metric' else f'Wind Speed: {wind_speed} mph')
    else:
        temperature_label.config(text='Weather information not available.')
        humidity_label.config(text='')
        wind_speed_label.config(text='')

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg='lightblue')

# Create and place widgets
tk.Label(root, text="City:", bg='lightblue', font=('Arial', 12)).pack(pady=5)
city_entry = tk.Entry(root, font=('Arial', 12))
city_entry.pack(pady=5)

tk.Label(root, text="Units:", bg='lightblue', font=('Arial', 12)).pack(pady=5)
units_var = tk.StringVar(value='Celsius')
units_menu = ttk.Combobox(root, textvariable=units_var, values=['Celsius', 'Fahrenheit'], state='readonly', font=('Arial', 12))
units_menu.pack(pady=5)

show_button = tk.Button(root, text="Show Weather", command=show_weather, font=('Arial', 12), bg='lightblue')
show_button.pack(pady=10)

temperature_label = tk.Label(root, text="", bg='lightblue', font=('Arial', 12))
temperature_label.pack(pady=5)

humidity_label = tk.Label(root, text="", bg='lightblue', font=('Arial', 12))
humidity_label.pack(pady=5)

wind_speed_label = tk.Label(root, text="", bg='lightblue', font=('Arial', 12))
wind_speed_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
