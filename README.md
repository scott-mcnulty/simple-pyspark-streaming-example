# Streaming POC

Simple app to test out spark streaming from Kafka.

First things first, set up a way to produce and consume from Kafka. Kafka setup using docker is outlined below with much of the setup credit going to @wurstmeister for his help at his [repo](https://github.com/wurstmeister/kafka-docker).

It's assumed that both `docker` and `docker-compose` are already installed on your machine to run this poc. `Java`, `Spark`, and `kafkacat` (optional but recommended) will also be used. Anything that needs to be installed is most likely going to be easiest when using Homebrew (such as kafkacat)

## Table of Contents

- [Streaming POC](#streaming-poc)
    - [Table of Contents](#table-of-contents)
    - [Links](#links)
    - [Playbook](#playbook)
        - [Single Node Kafka Cluster](#single-node-kafka-cluster)
        - [Multi Node Kafka Cluster](#multi-node-kafka-cluster)
        - [Words Producer and Consumer](#words-producer-and-consumer)
        - [Spark Streaming Application](#spark-streaming-application)

## Links

[Kafka docker image](https://hub.docker.com/r/wurstmeister/kafka/)  
[Run Kafka using docker](https://jaceklaskowski.gitbooks.io/apache-kafka/kafka-docker.html)  
[Kafka 0.10.0 example producer](https://kafka.apache.org/0100/javadoc/index.html?org/apache/kafka/clients/producer/KafkaProducer.html)  
[Kafkacat git repo](https://github.com/edenhill/kafkacat)  
[Kafkacat confluence](https://docs.confluent.io/current/app-development/kafkacat-usage.html)  
[Spark streaming + Kafka integration guide](https://spark.apache.org/docs/2.2.0/streaming-kafka-0-10-integration.html)  
[Kafka-python](https://pypi.org/project/kafka-python/)

## Playbook

After cloning this repo clone the repo below to get some Kafka docker-compose files:

```sh
cd streaming-poc;
git clone https://github.com/wurstmeister/kafka-docker.git
```

### Single Node Kafka Cluster

In the file `kafka-docker/docker-compose-single-broker.yml` change the `KAFKA_ADVERTISED_HOST_NAME` environment variable to use `localhost`.

Start a single node cluster with broker at localhost:9092.

```sh
docker-compose -f kafka-docker/docker-compose-single-broker.yml up -d
```

To verify the cluster was created successfully you can use a program like `kafkacat` to consume and produce to a topic.

In a new terminal use `kafkacat` to connect a consumer to the broker with topic `test`.

```sh
kafkacat -b localhost:9092 -C -t test
```

Add `-d broker` for debugging:

```sh
kafkacat -d broker -b localhost:9092 -C -t test
```

In another new terminal use `kafkacat` to connect a producer to the broker with topic `test`.

```sh
kafkacat -b localhost:9092 -P -t test
```

Type a message into the terminal and press enter to see the message consumed by the kafkacat consumer client.

[to top](#streaming-poc)

### Multi Node Kafka Cluster

TODO

[to top](#streaming-poc)

### Words Producer and Consumer

[Link to readme](words-producer-and-consumer-apps/README.md)

[to top](#streaming-poc)

### Spark Streaming Application

[Link to readme](streaming-app/README.md)

[to top](#streaming-poc)