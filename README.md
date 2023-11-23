# Velib Stations Monitoring

## Overview

This Python script utilizes Apache Spark and Elasticsearch to monitor Velib bike stations' status in real-time. The script reads data from a Kafka topic, processes it using PySpark, and indexes the relevant information into Elasticsearch. Additionally, it identifies and logs empty bike stations.

## Requirements

Ensure you have the following dependencies installed:

- `elasticsearch==8.10.1`
- `pyspark==3.5.0`
- `kafka-python==2.0.2`

You can install them using the following command:

```bash
pip install -r requirements.txt

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

Execute the script by running:

```bash
python velib_stations_monitoring.py
