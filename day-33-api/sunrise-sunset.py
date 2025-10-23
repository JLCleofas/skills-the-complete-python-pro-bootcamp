import requests

MY_LAT = 14.554729
MY_LONG = 121.024445

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'tzid': 'Asia/Singapore'
}

response = requests.get(
    'https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

print(sunset)
