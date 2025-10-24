import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = 'louie_cleofas@yahoo.com'
MY_PASSWORD = 'gapiambwctogkkzk'

MY_LAT = 14.554729
MY_LONG = 121.024445


def iss_overhead() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if 9 <= iss_latitude <= 20 and 116 <= iss_longitude <= 126:
        return True


def is_dark() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        'tzid': 'Asia/Singapore'
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now < sunrise or time_now > sunset:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        connection = smtplib.SMTP('smtp.mail.yahoo.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject: Look Up 👆🏽\n\nThe ISS is above you in the sky.'
        )
