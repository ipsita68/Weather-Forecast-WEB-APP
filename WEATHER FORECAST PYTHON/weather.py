import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
from PIL import Image, ImageTk
import pytz  # Add this import

# Create the root window
root = tk.Tk()
root.title("Weather APP")
root.geometry("900x500+300+200")
root.resizable(False, False)


# Function to fetch weather information
# Function to fetch weather information
def getWeather():
    city = textfield.get()

    # Geocoding
    geolocator = Nominatim(user_agent="WeatherApp")
    location = geolocator.geocode(city)
    if not location:
        messagebox.showerror("Error", "City not found")
        return

    # Timezone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Weather API
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=da084e3d8a1642c137abfae81b2f3d92"
    try:
        json_data = requests.get(api_url).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Updating labels with weather information
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description)
        p.config(text=f"{pressure} Pa")

    except Exception as e:
        messagebox.showerror(
            "Error", f"Failed to fetch weather data: {str(e)}")


# Search box
Search_image = ImageTk.PhotoImage(file="search.png")
myimage = tk.Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify='center', width=17,
                     font=('poppins', 25, 'bold'), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

# Search button
search_icon = ImageTk.PhotoImage(file="search_icon.png")
search_button = tk.Button(image=search_icon, borderwidth=0,
                          cursor="hand2", bg="#404040", command=getWeather)
search_button.place(x=400, y=34)

# Logo
logo_image = ImageTk.PhotoImage(file="logo.png")
logo = tk.Label(image=logo_image)
logo.place(x=150, y=100)

# Clock
name = tk.Label(root, font=("arial", 15, 'bold'))
name.place(x=30, y=100)
clock = tk.Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Bottom box
frame_image = ImageTk.PhotoImage(file="box.png")
frame_myimage = tk.Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

# Labels
label1 = tk.Label(root, text="WIND", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="HUMIDITY", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = tk.Label(root, text="PRESSURE", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Weather information labels
t = tk.Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = tk.Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=113, y=430)

h = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=280, y=430)

d = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=445, y=430)

p = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=670, y=430)

# Run the main event loop
root.mainloop()
