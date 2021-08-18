#!/bin/bash
# Change dictory to kafka server
cd /usr/local/kafka/

# create stockTwits topic
bin/kafka-topics.sh --create --topic stockTwitsStream --bootstrap-server localhost:9092