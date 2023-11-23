import json
import time
import urllib.request
from kafka import KafkaProducer
from datetime import datetime

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    response = urllib.request.urlopen(url)
    stations_data = json.loads(response.read().decode())

    for station in stations_data:
        # Check if 'position' key exists
        if 'position' in station and station['last_update']:
            utcfromtimestamp = datetime.utcfromtimestamp(int(station['last_update'])/1000).strftime('%Y-%m-%d %H:%M:%S')
            # Check if 'lat' and 'lng' keys exist under 'position'
            latitude = station["position"]["lng"] if "position" in station and "lat" in station["position"] else None
            longitude = station["position"]["lat"] if "position" in station and "lng" in station["position"] else None
            # Extract relevant fields to match the consumer schema
            formatted_station = {
                "number": station["number"] if "number" in station else None,
                "contractName": station["contract_name"] if "contract_name" in station else "",
                "name": station["name"] if "name" in station else "",
                "address": station["address"] if "address" in station else "",
                "last_update":utcfromtimestamp,
                "position": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "totalStands": {
                    "availabilities": {
                        "bikes": station["available_bikes"] if "available_bikes" in station else 0,
                        "stands": station["bike_stands"] if "bike_stands" in station else 0
                    },
                    "capacity": station["bike_stands"] if "bike_stands" in station else 0
                }
            }


        # Send formatted data to Kafka topic
        producer.send("velib-stations", json.dumps(formatted_station).encode())

    print("{} Produced {} station records".format(time.time(), len(stations_data)))
    time.sleep(1)