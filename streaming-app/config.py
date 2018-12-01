
# Spark configs
master = "local[1]"
app_name = "PysparkStreamingFromKafka"
streaming_window_size = 10

# Kafka configs
brokers = "localhost:9092"
consumer_group_id = "10"
topics = ["test"]

# Configs for the producer script
topic = "test"
x_data_path = "./model/data/X.csv"
producer_sleep_time = .7 # sleep is in seconds
bytes_encoding = "UTF-8"
