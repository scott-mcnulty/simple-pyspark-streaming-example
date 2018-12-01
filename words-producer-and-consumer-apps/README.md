# Words Producer and Consumer

First verify that a kafka cluster is up and running such as the single node cluster outlined in the root README.md.

The supplied jars act as a producer and consumer to the kafka topic. Run each of the jars in separate terminals to see the messages being produced and consumed. The consumer works by reading in a file containing many words (`words.txt`) and sending a random handful as a message to the topic. Producer output should be like:

```sh
Sent message: undisturbedly archmugwump debouchure dispersals straw-shoe decaspermous featherman paegel
Sent message: puppyfoot postoffices surnape strophically allyl Holt tatouays sternly wayman
Sent message: cumsha palaeopsychology punkin Gerlachovka macrencephaly
Sent message: unexplainableness convell
Sent message: dialogged flaggers nightflit zygoma unattached beant antiscians
Sent message: colluviums unsacramental
Sent message: Pro-zionism rathest Maypole atypy bestudded night-fly
Sent message: phthoric cynegetics Feosol micromazia felted
Sent message: sacrocoxalgia interlunar parang heart-whole Gaelic pairing workout azure-penciled
Sent message: Pinz Dmitrov drop-leaf peins Buyse xylindein
```

The consumer should produce output like:

```
Received message: (1306, Clethra solitude self-propulsion ) with word count `3` at offset 1306
Received message: (1307, laemostenosis ablegate ) with word count `2` at offset 1307
Received message: (1308, Bergwall vedana half-cocked Haiti forgettable cracklings Camas ) with word count `7` at offset 1308
Received message: (1309, Soekarno theorematic pyrometamorphic Phacidiales unqueme understeer self-shelter anteprandial syrringing ) with word count `9` at offset 1309
Received message: (1310, Physostegia Teredinidae january's pentalpha exogastritis casaques interglyph chiv ) with word count `8` at offset 1310
Received message: (1311, USV jambes thisness Aracaju Coralville Collettsville ) with word count `6` at offset 1311
Received message: (1312, submontagne ) with word count `1` at offset 1312
Received message: (1313, Sapphira wearifully swingby soojee ethchlorvynol Proto-chaldaic landfill libels epexegetically massed ) with word count `10` at offset 1313
Received message: (1314, Subotica picture-seeking prosed parabolize predefect trans-pacific Kashube wlecche agalaxia ) with word count `9` at offset 1314
Received message: (1315, unsymmetrically protaspis ) with word count `2` at offset 1315
Received message: (1316, askaris Murage allegorizing thorianite Bron promerger superglottally albuminised ) with word count `8` at offset 1316
Received message: (1317, jactance mountaintop advoke ganglioside sudations diffusivity Neisse latened ) with word count `8` at offset 1317
Received message: (1318, span-new piacularly soft-flecked gowl ) with word count `4` at offset 1318
Received message: (1319, phasic saxhorns Bombycina ) with word count `3` at offset 1319
```

## Sending Messages to the Cluster

In the original terminal use the `javaKafkaProducer.jar` to send messages to the cluster. To see parameter usage run:

```sh
java -jar javaKafkaProducer.jar
```

Below is an example run command using the topic `test` that was created within the `kafka-docker/docker-compose-single-broker.yml` file.

```sh
java -jar javaKafkaProducer.jar "localhost:9092" "10" "./words.txt" "10000" "test"
```

Switch back to the terminal running the kafkacat consumer and you should see the consumer consuming messages that are being sent to the topic. Within the terminal running the jar hit `ctrl + c` to stop producing messages.

## Consuming Messages from the Cluster

In a different terminal use the `scalaKafkaConsumer.jar` to consume messages from the cluster.

- Arg 0: brokers
- Arg 1: group id
- Arg 2: topic

```sh
java -jar scalaKafkaConsumer.jar "localhost:9092" "10" "test"
```