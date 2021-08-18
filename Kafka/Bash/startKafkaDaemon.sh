#!/bin/bash
# Change dictory to kafka server
cd /usr/local/kafka/

# start kafka daemon
bin/kafka-server-start.sh config/server.properties
