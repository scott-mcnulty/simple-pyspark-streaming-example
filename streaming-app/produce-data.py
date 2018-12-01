import csv
import random
import json
import time
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from kafka import KafkaProducer

import config as config

def main():

    # Get x data from csv
    with open(config.x_data_path) as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]

    # Set up the producer
    producer = KafkaProducer(bootstrap_servers=config.brokers)

    # Get n number of random rows from the csv data to send to the topic
    for row in rows:
        data = [dict(rows[random.randrange(0, len(rows))])]
        logging.info("Sending message: `{}` as bytes using encoding {}".format(data, config.bytes_encoding))
        producer.send(config.topic, bytes(json.dumps(data), config.bytes_encoding))
        time.sleep(config.producer_sleep_time)

    producer.close()


if __name__ == '__main__':

    main()