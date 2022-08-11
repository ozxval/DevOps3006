import requests
try:
    res = requests.get("httpsuu://github.com")
except Exception as e:
    print(e.args)
try:
    f = int(input("df:"))
    r = 5 / 0
except ZeroDivisionError:
    print("cant div")
except ValueError:
    print("number")