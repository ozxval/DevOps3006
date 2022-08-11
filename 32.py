import requests
iist = ["http://localhost:5001/whatismyname", "http://localhost:5001/",
        "http://localhost:5001/2133"]
for i in iist:
    res = requests.post(i)
    print(res.text)