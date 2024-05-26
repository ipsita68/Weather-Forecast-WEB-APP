
---

# Weather Forecast Web App

Weather Forecast Web App is a web-based application designed to provide users with real-time weather information for any location worldwide. Built using Python and Tkinter, this application offers a user-friendly interface and displays various weather parameters such as temperature, wind speed, humidity, and atmospheric pressure.

## Functionality

Weather Forecast Web App provides the following key features:

1. **Real-time Weather Information**: Fetches up-to-date weather data from the OpenWeatherMap API based on the user-entered city, providing accurate weather conditions such as temperature, humidity, wind speed, and more.

2. **Location Search**: Allows users to search for weather information by entering the name of the desired city, enabling quick access to weather forecasts for various locations worldwide.

3. **Geocoding Integration**: Utilizes the Geopy library to geocode the city name and obtain its coordinates for weather data retrieval. This ensures precise weather information corresponding to the specified location.

4. **Timezone Display**: Displays the current local time for the entered city based on its geographical coordinates, enhancing user experience by providing relevant time information alongside weather forecasts.

5. **Interactive Map Display**: Incorporates an interactive map feature using Folium, allowing users to visualize the location of the selected city on a map. This enhances spatial understanding and provides users with a comprehensive view of the city's geographical context.

6. **Error Handling Mechanism**: Provides robust error handling to manage scenarios where the entered city is not found or there are issues with fetching weather data. Informative error messages guide users on how to proceed effectively in such cases.

These features collectively create a comprehensive and user-friendly weather forecasting application, empowering users to access accurate weather forecasts and geographical insights seamlessly.

## GUI Design

Weather Forecast Web App utilizes Tkinter for its GUI design, ensuring a responsive layout and clean interface. The application's design adheres to Tkinter's styling guidelines, providing a visually appealing and user-friendly experience.

## Personal Contributions

As the developer of Weather Forecast Web App, I played a significant role in designing and implementing the front-end components and functionality using Python and Tkinter. Additionally, I integrated external APIs and libraries to fetch weather data and enhance the application's features. My contributions aimed to provide users with a reliable and efficient weather forecasting tool.

## How to Use

To use the Weather Forecast Web App, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the `weather.py` script using Python.
4. Enter the name of the city for which you want to fetch weather information in the provided search box.
5. Click the search button to fetch and display the weather forecast for the entered city.


## Screenshot of the web-app:
![image](https://github.com/ipsita68/Weather-Forecast-WEB-APP/assets/121110612/489233df-2af8-4d2e-bb02-fb416128f2bc)

## Credits

- **Geopy**: Used for geocoding city names to obtain their coordinates.
- **OpenWeatherMap API**: Used for fetching real-time weather data.
- **PIL (Python Imaging Library)**: Used for handling images in the GUI.
- **pytz**: Used for handling timezones and displaying local time for the entered city.

---
