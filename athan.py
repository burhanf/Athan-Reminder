from calendar import c
from re import S


class Athan:
    def __init__(self, sunrise, fajr, dhuhr, asr, maghrib, sunset, isha, city):
        self.sunrise = sunrise
        self.fajr = fajr
        self.dhuhr = dhuhr
        self.asr = asr
        self.maghrib = maghrib
        self.sunset = sunset
        self.isha = isha
        self.city = city
