import requests
from athan import Athan


def main():
    athanTimes = Athan("", "", "", "", "", "", "", "")
    getAthanTimes(athanTimes)


    print(athanTimes.sunrise)

    sendEmail()


def getAthanTimes(athanTimes):
    # API for athan
    # https://prayertimes.date/api/docs/today
    athanResponse = requests.get(
        "https://api.pray.zone/v2/times/today.json?city=mississauga")

    if (athanResponse.status_code != '404'):
        athanResponseObject = athanResponse.json()['results']

        times = athanResponseObject['datetime'][0]['times']
        location = athanResponse.json()['results']['location']['city']

        # create athan object
        athanTimes.sunrise = times['Sunrise']
        athanTimes.fajr = times['Fajr']
        athanTimes.dhuhr = times['Dhuhr']
        athanTimes.asr = times['Asr']
        athanTimes.maghrib = times['Maghrib']
        athanTimes.sunset = times['Sunset']
        athanTimes.isha = times['Isha']
        athanTimes.location = location
    else:
        print("Error obtaining Athan times")


def sendEmail():
    # Send email to SMS
    # https://realpython.com/python-send-email/
    pass


# main
main()
