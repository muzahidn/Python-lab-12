import requests


def get_coordinates(api_key, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['coord']['lat'], data['coord']['lon']
    else:
        print("Error fetching coordinates.")
        return None, None


def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['weather'][0]['description'], data['main']['temp']
    else:
        print("Error fetching weather.")
        return None, None


def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15)


def main():
    api_key = "ebfa9db575fa05f04db390941d8a00a0"  
    city_name = input("Enter the name of the municipality:\n")

    lat, lon = get_coordinates(api_key, city_name)
    if lat is not None and lon is not None:
        description, temp_kelvin = get_weather(api_key, lat, lon)
        if description is not None and temp_kelvin is not None:
            temp_celsius = kelvin_to_celsius(temp_kelvin)
            print(f"Weather: {description.capitalize()}")
            print(f"Temperature: {temp_celsius}°C")
        else:
            print("Unable to fetch weather information.")
    else:
        print("Unable to fetch coordinates for the given city.")


main()

