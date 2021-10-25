import streamlit as st
import requests
import json
from db import Weather, opendb
from datetime import datetime


def read_credentials():
    '''Read the different parameters for the API call.
    '''
    with open("files/credentials.json", "r") as file:
        data = file.read()
    return json.loads(data)


def api_call():
    '''API call using credentials as defined in the following link.
    https://openweathermap.org/current.
    '''
    obj = read_credentials()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url + "&".join([f'{k}={v}' for k,v in obj.items()])
    weather_data = requests.get(final_url)
    return weather_data


def main():
    timedate = datetime.now()
    
    # Display
    st.title("Task 2: API Call")
    col1, col2 = st.columns([3, 1])
    if col2.checkbox('"Today is prime"', value=False):
        timedate = timedate.replace(day=1)
    col1.subheader(f'Solar Radiation from Today ({timedate.date()}):')

    # Exception
    if timedate.day == 1:
        st.warning('HTTP 503 (Service Unavailable) :\nDate is prime, so no data')
    
    # API call
    else:
        weather_data = api_call()
        if weather_data.status_code == 200:
            db = opendb()
            weather = Weather(date=timedate, json=weather_data.json())
            db.add(weather)
            db.commit()
            db.close()
            
            # Display
            st.json(weather_data.json())
        else:
            st.error(f'Status Code = {weather_data.status_code}')
        
    st.caption("From [OpenWeatherMap API](https://openweathermap.org/current)")


if __name__ == "__main__":
    main()