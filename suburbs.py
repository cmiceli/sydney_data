import requests
import json

results = []
KEY = None

with open("suburbs.csv", 'r') as f:
    for line in f:
        l = line.strip().split(",")
        burbs = "{}+{}".format(l[0].replace(" ", "+"), l[1])
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}+NSW&destinations=Town+Hall+Sydney&mode=transit&transit_mode=rail&key={}&departure_time=1484116200".format(burbs, KEY)
        r = requests.get(url)
        results.append(json.loads(r.text))

print(json.dumps(results))
