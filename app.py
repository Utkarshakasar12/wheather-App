import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("Wheather_API_KEY")

st.set_page_config(page_title="Weather App", page_icon=":smiley:")
st.title("Weather App ⛅")
st.write("Enter a city name and press the button to get the current weather information.")

city = st.text_input('Enter City Name')
if(st.button("Get Weather")):
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(API_URL)
    if (response.status_code == 200):
        st.success("Weather data fetched successfully!")    
        data = (response.json())
        temperature = data['main']['temp'] # extract data in variable
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['main']
        country = data['sys']['country']
        name = data['name']

        st.header(f'{name}, {country}')
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        # Display the weather information
        col1.metric('Temperature', f"{temperature}°C 🌡️")    
        col2.metric('Humidity', f"{humidity}% 💧")
        col3.metric('Wind Speed', f"{wind_speed} m/s 🌬️")
        col4.write('Condition:' f"{condition}🕒")

    else:
        st.error("City not found. Please check the city name and try again.")