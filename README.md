# Velib Stations Monitoring

## Overview

This Python script utilizes Apache Spark and Elasticsearch to monitor Velib bike stations' status in real-time. The script reads data from a Kafka topic, a distributed streaming platform, processes it using PySpark, and indexes the relevant information into Elasticsearch. After that, we can perform data visualizations using Kibana, taking advantage of the powerful analytics capabilities provided by the Elasticsearch-Kibana stack. Additionally, it identifies and logs empty bike stations, providing valuable insights into station utilization and availability.


## Requirements

Ensure you have the following dependencies installed:

- `elasticsearch==8.10.1`
- `pyspark==3.5.0`
- `kafka-python==2.0.2`

You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Setup

### Elasticsearch Setup:

1. Make sure Elasticsearch is running on `localhost:9200`.
2. The script creates an index named "velib-stations." If it already exists, it deletes and recreates it.

### Kafka Setup:

- The pyspark_code.py script reads data from a Kafka topic named "velib-stations" on `localhost:9092`.
- That Kafka topic was created in the file get_stations.py
- In the file get_stations.py change the API key with yours after creating an account at https://developer.jcdecaux.com/#/opendata/vls?page=getstarted

### Spark Configuration:

- The Spark session is configured to connect to Elasticsearch on `localhost:9200`.

## Running the Script

Before executing the main pyspark_consumer.py, ensure that Zookeeper and Kafka servers are running. You can start them using the following commands in different terminals and IN THAT ORDER:

1. Start Zookeeper:

   ```bash
   ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
2. Start Kafka
    ```bash
   ./bin/kafka-server-start.sh ./config/server.properties
3. Run the get_stations.py file by doing
    ```bash
   python3 Stations_producer.py

after that you can run the main script with spark-submit
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark_consumer.py
```
# Kibana Visualizations 

## Kibana Dashboard

![Kibana Dashboard](images/dashboard.png)

*Description:* This image displays the Kibana dashboard.

## Global Map

![Global Map](images/global_map.png)

*Description:* This image provides an overview of the stations map in Europe.

## Valencia City Map

![Valencia City Map](images/valencia_stations.png)

*Description:* This image presents the map for bike stations and their capacity in the city of Valencia.

## Bike Count Evolution in 3 Chosen Cities

![Bike Count Evolution](images/bike_evolution_3_cities.png)

*Description:* This image illustrates the evolution of bike counts in three selected cities: Brussels, Tokyo, and Valencia.

![Bike Count Evolution](images/3_diff_cities.png)

*Description:* When hovering over the plot, the number of bikes in each city appears in the window.

## Latest Bike Counts Table

![Latest Bike Counts Table](images/last_number_of_bikes.png)

*Description:* This image features the latest bike counts in different cities in the last 30 seconds.
