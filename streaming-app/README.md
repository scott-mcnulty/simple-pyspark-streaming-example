# Streaming App

Simple pyspark streaming application to read in data from a kafka topic. A model within the streaming app is predicting on the datapoints as they are consumed.

Before running, verify that a kafka cluster is up and running such as the single node cluster outlined in the root [README.md](../README.md). Install the necessary python packages using the `requirements.txt` file (virtualenv recommended).

## Versions

Tested with `Spark 2.2.1` using `Scala version 2.11.8`, `Java` HotSpot(TM) 64-Bit Server VM, `1.8.0_181`.  
You may need to change what jar is supplied in the `spark-submit` command to match the `kafka version` you're running.  
`Python3 version 3.6.4`.

## Playbook

Update the `config.py` file with any necessary configurations

Run the app using the command:

```sh
spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.0.jar spark-streaming.py
```

In a new terminal run `kafkacat` again as a producer to begin sending messages.

```sh
kafkacat -b localhost:9092 -P -t test
```

Use the example messages within the `example-messages.txt` file to see example data points that can be given to the app model to predict on. Messages printed out in the terminal running the spark job is a package where the first item is the data points and the second is the prediction e.g. (datapoints, prediction).

Below is example output from the application:

```
([{'CRIM': 0.09849, 'ZN': 0.0, 'INDUS': 25.65, 'CHAS': 0.0, 'NOX': 0.581, 'RM': 5.879, 'AGE': 95.8, 'DIS': 2.0063, 'RAD': 2.0, 'TAX': 188.0, 'PTRATIO': 19.1, 'B': 379.38, 'LSTAT': 17.58}], 16.46)
```

## Produce Data Script

If instead you'd like to have data sent to the kafka topic automatically the python script `produce-data.py` can be used. Be sure to run `pip install -r requirements.txt` (virtualenv recommended) so you have all of the necessary python packages. Run the command to start the script:

```sh
python3 produce-data.py
```