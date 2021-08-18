#!/bin/bash
# Change dictory to kafka server
cd /usr/local/kafka/

#create stockData topic
bin/kafka-topics.sh --create --topic stockData --bootstrap-server localhost:9092
