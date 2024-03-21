import requests
import json
import datetime

currentTime = datetime.datetime.now()
formattedTime = currentTime.strftime("%d-%m-%Y %H:%M:%S")

print(f'Start: {formattedTime}')

url = "https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()   
else:
    print(f"cant connect, status code:  {response.status_code}")

texts = []

for dayData in data["data"]["Rows"]:
    #print(dayData)
    for filterRows in dayData["Columns"]:
        #print(filterRows)
        texts.append(filterRows)

        if filterRows["Index"] == 0:
            if filterRows["CombinedName"] == "LV":
                continue
            #print(filterRows["CombinedName"] + " - " + filterRows["DateTimeForData"] + " - " + filterRows["Value"])
            #splitedTime = filterRows["DateTimeForData"].split("T")

            #texts = [filterRows]
            filePath = "/home/ek/Downloads/save_data.txt"
            jsonFilePath = "/home/ek/Downloads/collectedDataJson.json"
            with open(filePath, "w") as file:
                json.dump(texts, file, indent=4)
                #file.write("\n") 
            with open(jsonFilePath, "w") as file:
                json.dump(texts, file)
            
        #print(filterRows)      

currentEndTime = datetime.datetime.now()
formattedEndTime = currentEndTime.strftime("%d-%m-%Y %H:%M:%S")

#print(response.status_code)
print(f"Done: {formattedEndTime}")