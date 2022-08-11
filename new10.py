import datetime
import requests


def ison(site):
    if site.status_code == 200:
        print("is on")
    else:
        print("is off")


url = requests.get(input("enter your website: "))
ison(url)
