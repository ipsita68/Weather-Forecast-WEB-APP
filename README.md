
---

# Weather Forecast Web App

Weather Forecast Web App is a web-based application designed to provide users with real-time weather information for any location worldwide. Built using Python and Tkinter, this application offers a user-friendly interface and displays various weather parameters such as temperature, wind speed, humidity, and atmospheric pressure.

## Functionality

Weather Forecast Web App provides the following key features:

- **Weather Information**: Fetches real-time weather data from the OpenWeatherMap API based on the user-entered city.
- **Location Search**: Allows users to search for weather information by entering the name of the desired city.
- **Geocoding**: Utilizes the Geopy library to geocode the city name and obtain its coordinates for weather data retrieval.
- **Timezone Display**: Displays the current local time for the entered city based on its geographical coordinates.
- **Error Handling**: Provides error messages for cases where the entered city is not found or if there is an issue with fetching weather data.

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

## Credits

- **Geopy**: Used for geocoding city names to obtain their coordinates.
- **OpenWeatherMap API**: Used for fetching real-time weather data.
- **PIL (Python Imaging Library)**: Used for handling images in the GUI.
- **pytz**: Used for handling timezones and displaying local time for the entered city.

---
