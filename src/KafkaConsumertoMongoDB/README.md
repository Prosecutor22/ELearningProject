After the previous step to stream data from Moodle to Kafka producer. Now, we will stream data from Kafka Logs to MongoDB.

Run:

```bash
   cd KafkaConsumertoMongoDB
```
Instead of printing the logs output the terminal, we will write data generated from user activities in Moodle to file **log.txt**

```bash
$ docker run -it --rm \
    --network moodlekafkaproducer_default \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 \
    bitnami/kafka:3.1 kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic saturday-test --from-beginning > log.txt
```
After that, we want to extract logs as a json files. But a problem is that the data in log.txt is not formatted in json type. 

Therefore, we have to preprocessing data to multiple logs that each blog is one action that user interact in Moddle.

Run **preprocessing.py**:

```bash
   python preprocessing.py
```
After that, It will generate for you logs about interaction of user in Moddle. Remember that, each log is a interaction of user.

In sample logs, we generate 14 logs. It means that user interact 14 activities with Moodle.

And these logs will be streamed to MongoDB and turn to Spark to analyst.

```bash
mongoimport --jsonArray --db test --collection docs --file filename.json
```
