
# Standard python lib
import json

# 3rd parth libs
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# Our libs
from model import predict
import config as config


def main():

    # Create a local StreamingContext with two working thread and batch interval of 1 second
    sc = SparkContext(
        config.master, 
        config.app_name
    )

    # n second window
    ssc = StreamingContext(
        sc, 
        config.streaming_window_size
    )

    # Subscribe to the topic
    kafkaStream = KafkaUtils.createDirectStream(
        ssc, 
        config.topics,
        {'metadata.broker.list': config.brokers}
    )

    # Get the messages from the topic
    messages = kafkaStream.map(lambda message: message)
    # messages.pprint()

    # Get the data points from each message
    data_points = messages.map(lambda data: json.loads(data[1]))
    # data_points.pprint()

    # Make a prediction for each data point and package as (data_points, prediction)
    # Predicts: median price (thousands)
    predictions = data_points.map(lambda data_point: (data_point, predict.predict(data_point[0])))
    predictions.pprint()

    ssc.start()
    ssc.awaitTermination()



if __name__ == '__main__':

    main()