#!/bin/bash
# Change dictory to kafka server
cd /usr/local/kafka/

# create twitter topic
bin/kafka-topics.sh --create --topic twitterStream --bootstrap-server localhost:9092
