from tkinter import *
from PIL import Image, ImageTk
import requests
from datetime import datetime
from geopy.geocoders import Nominatim

class RoundedButton(Button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.config(relief=FLAT, bg="#E74C3C", fg="blue", bd=0, highlightthickness=0)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.show_weather)

    def on_enter(self, e):
        self.config(bg="#C0392B")

    def on_leave(self, e):
        self.config(bg="#E74C3C")

    def show_weather(self, event):
        showWeather()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def get_location_details(latitude, longitude):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.reverse((latitude, longitude), language='en')
    
    if location:
        address = location.address
        location_details = {
            'Country': location.raw.get('address', {}).get('country', ''),
            'State': location.raw.get('address', {}).get('state', ''),
            'City': location.raw.get('address', {}).get('city', ''),
            'Suburb': location.raw.get('address', {}).get('suburb', ''),
            'Road': location.raw.get('address', {}).get('road', ''),
        }
        return location_details
    else:
        return {}

def showWeather():
    api_key = "b301d78eb0e1c20c139d78557b7a1ed8"  # sample API
    city_name = city_value.get()

    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()

    tfield.config(state=NORMAL)
    tfield.delete("1.0", "end")

    if weather_info['cod'] == 200:
        kelvin = 273
        temp_celsius = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp_celsius = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        latitude = weather_info['coord']['lat']
        longitude = weather_info['coord']['lon']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"Weather in {city_name.upper()}:\n"
        weather += f"Temperature: {temp_celsius}°C\n"
        weather += f"Feels like: {feels_like_temp_celsius}°C\n"
        weather += f"Pressure: {pressure} hPa\nHumidity: {humidity}%\n"
        weather += f"Wind Speed: {wind_speed:.2f} km/h\n\n"
        weather += f"Sunrise: {sunrise_time}\nSunset: {sunset_time}\n"
        weather += f"Cloudiness: {cloudy}%\nDescription: {description}\n"

        # Get location details using reverse geocoding
        location_details = get_location_details(latitude, longitude)
        
        # Display location details
        details_text = "\n".join(f"{key}: {value}" for key, value in location_details.items() if value)
        
        tfield.tag_configure('center', justify='center')
        tfield.config(state=NORMAL, bg="lightblue", fg="black", height=17)  # Set the height based on your preference
        tfield.insert(INSERT, weather, 'center')
        tfield.insert(INSERT, f"\nLocation Details:\n{details_text}\n", 'center')
        tfield.config(state=DISABLED)
    else:
        error_message = f"\n\tWeather for '{city_name}' not found!\n\tPlease enter a valid city name."
        # error_label.config(text=error_message, fg="red")

        # Set the size for the error message box
        tfield.config(state=NORMAL, bg="red", fg="black", height=5)  # Set the height based on your preference
        tfield.insert(INSERT, error_message, 'center')
        tfield.config(state=DISABLED)

    tfield.place(relx=0.5, rely=0.55, anchor=CENTER)
    tfield.config(state=DISABLED)

root = Tk()
root.geometry("1200x800")

root.title("Designful Weather App")

# Background Image
bg_image = Image.open("D:/CODEWAY INTERNSHIP/weather.jpg")  # Replace with the path to your image
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# City Input
city_label = Label(root, text='Enter City Name:', font=('Helvetica', 24), bg='black', fg='white', pady=2)
city_label.place(relx=0.2, rely=0.1, anchor=CENTER)

city_value = StringVar()
city_entry = Entry(root, textvariable=city_value, width=30, font=('Helvetica', 20), bd=3, relief=SOLID)
city_entry.place(relx=0.5, rely=0.1, anchor=CENTER)

# Button
weather_button = RoundedButton(root, text="Show Weather", font=("Helvetica", 20, 'bold'))
weather_button.place(relx=0.8, rely=0.1, anchor=CENTER)

# Error Label
error_label = Label(root, text="", font=('Helvetica', 16), fg='red', bg='red')

error_label.place(relx=0.5, rely=0.2, anchor=CENTER)
error_label.place_forget()

# Weather Display
tfield = Text(root, width=50, wrap=WORD, bd=0, highlightthickness=0, state=DISABLED, font=('Helvetica', 20), bg="lightblue")
tfield.place_forget()

root.mainloop()
