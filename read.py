import json

#Sis bus read  prieks first.py
print("Start")
filePath = "/home/ek/testa-repo/collectedDataJson.json"

with open(filePath, "r") as file:
    data = json.load(file)

for specificData in data:
    if specificData["Index"] == 0:
        if specificData["Name"] == "LV":
            continue
        print(specificData["Name"] + " - " + specificData["DateTimeForData"] + " - " + specificData["Value"] + " Eur")
#asd
print("Done")