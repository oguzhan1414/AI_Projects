
import requests
API_KEY = "087ff3ca862852893fa29f4abef86c80"
city = "London"
#url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City" : data["name"],
                "Temperature" : f"{data["main"]["temp"]}C",
                "Weather": data["weather"][0]["description"].title(),

            }
            return weather
        elif response.status_code == 404:
            print("Şehir bulunamadı")
        else:
            print("Başka bir hata")
    except Exception as e:
        print("Nadir hata",e)

    return None


def display_weather(weather):
    print("Hava durumu bilgileri")
    for key,value in weather.items():
        print(f"{key}: {value}")

while True:
    print("-----Weather App---------")
    city = input("Şehir ismi giri").strip()
    if city.lower() == "q":
        break
    weather = get_weather(city)
    if weather:
        display_weather(weather)