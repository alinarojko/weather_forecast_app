# Import library to receive data from url
import requests

# API keys for registered user on the actual website
API_KEY = "7c490bd16f5c494d9c60e0826cd87935"

# Define the function which will request from user 3 parameters
def get_data(place, days=None, kind=None):

    # Url is taken from the website like example
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    # Responce - check for the data on the url , and collect it to the variable with request method in json format
    responce = requests.get(url)
    data = responce.json()

    # Operate within the collected data , open debugger and check where is our data is stored
    # filter collected data  by the "list" parameter
    filtered_data = data["list"]

    # The full data list contain for us 40 small list with temperature , 8 for each day
    # So to see the value of the temperature for  user entered {days} , we filter it

    filtered_data = filtered_data[:8*days]

    # Check for the type user selected "temperature or sky"
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    get_data(place="Tokio", days=3, kind="Temperature")