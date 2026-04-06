import requests

API_KEY = "b056a9ff210d46eb278887ecc91eccc7"
CITY = "Navi Mumbai"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"City: {CITY}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")
else:
    print("Error:", data)