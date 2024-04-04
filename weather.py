import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
from PIL import Image, ImageTk
import pytz
import folium
import io


# Create the root window
root = tk.Tk()
root.title("Weather APP")
root.geometry("1400x600+200+100")
root.resizable(False, False)


def getWeather():
    city = textfield.get()

    # Geocoding
    geolocator = Nominatim(user_agent="WeatherAPP")
    location = geolocator.geocode(city, timeout=20000)
    if not location:
        messagebox.showerror("Error", "City not found")
        return

    # Timezone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    # Fetch latitude and longitude coordinates
    lat = location.latitude
    lon = location.longitude
    print(lat)
    print(lon)

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

        # Display map
        displayMap()

    except Exception as e:
        messagebox.showerror(
            "Error", f"Failed to fetch weather data: {str(e)}")


def displayMap():
    city = textfield.get()

    # Geocoding
    geolocator = Nominatim(user_agent="WeatherAPP")
    location = geolocator.geocode(city, timeout=20000)
    if not location:
        messagebox.showerror("Error", "City not found")
        return

    # Create folium map
    m = folium.Map(location=[location.latitude,
                   location.longitude], zoom_start=10)

    # Generate PNG image from the map
    img_data = m._to_png()

    # Convert PNG image data to PhotoImage
    map_photo = ImageTk.PhotoImage(data=img_data)

    # Display folium map as an image in Tkinter
    map_label.config(image=map_photo)
    map_label.image = map_photo


# icon
image_icon = tk.PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Search box
# Calculate the x-coordinate for the search box to center it horizontally
search_box_width = 17
window_width = 1400  # Width of the window
search_box_x = (window_width - search_box_width * 25) // 2
Search_image = ImageTk.PhotoImage(file="search.png")
myimage = tk.Label(image=Search_image)
myimage.place(x=search_box_x, y=20)
textfield = tk.Entry(root, justify='center', width=17,
                     font=('poppins', 25, 'bold'), bg="#404040", border=0, fg="white")
textfield.place(x=search_box_x+70, y=40)
textfield.focus()

# Bind the Return key event to getWeather function
textfield.bind("<Return>", lambda event: getWeather())

# Search button
search_icon = ImageTk.PhotoImage(file="search_icon.png")
search_button = tk.Button(image=search_icon, borderwidth=0,
                          cursor="hand2", bg="#404040", command=getWeather)
search_button.place(x=search_box_x+380, y=34)

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
frame_myimage.place(x=10, y=370)

# Labels
label1 = tk.Label(root, text="WIND", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=60, y=400)

label2 = tk.Label(root, text="HUMIDITY", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=200, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=380, y=400)

label4 = tk.Label(root, text="PRESSURE", font=(
    'Helvetica', 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=600, y=400)

# Weather information labels
t = tk.Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = tk.Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=60, y=430)

h = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=230, y=430)

d = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=350, y=430)

p = tk.Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=600, y=430)

# Map label
map_label = tk.Label(root)
# Adjust width and height as needed
map_label.place(x=800, y=100, width=500, height=400)

# Run the main event loop
root.mainloop()
