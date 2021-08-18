#!/bin/bash
# Change dictory to kafka server
cd /usr/local/kafka/
# start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# start kafka daemon
bin/kafka-server-start.sh config/server.properties

#create stockData topic
bin/kafka-topics.sh --create --topic stockData --bootstrap-server localhost:9092

# create twitter topic
bin/kafka-topics.sh --create --topic twitterStream --bootstrap-server localhost:9092

# create stockTwits topic
bin/kafka-topics.sh --create --topic stockTwitsStream --bootstrap-server localhost:9092