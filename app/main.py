import requests
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is not set.")
        return
    else:
        url = "http://api.weatherapi.com/v1/current.json?"
        filtering = "Paris"
        result = requests.get(url + f"key={api_key}&" + f"q={filtering}")
        if result.status_code == 200:
            data = result.json()
            city = data["location"]["name"]
            country = data["location"]["country"]
            day_time = data["location"]["localtime"]
            temperatura = data["current"]["temp_c"]
            type_weather = data["current"]["condition"]["text"]
            print(f"{city}/{country} {day_time} "
                  f"Weather: {temperatura} {type_weather}")
        else:
            print("Error: invalid request")


if __name__ == "__main__":
    get_weather()
