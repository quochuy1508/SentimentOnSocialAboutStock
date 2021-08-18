from kafka import *
import datetime as dt
import os
import time
import sys
import requests

# kafka setup
producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
topicName = 'stockData'
path = '/tmp/marketstack-logs/'


def doWork(ticker, exchange):
    while True:
        date = dt.datetime.now().strftime("%Y%m%d")
        # if dt.datetime.now().hour >14 or dt.datetime.now().hour<6:
        # time.sleep(3600) # sleep for an hour at night

        fileNameNew = path + ticker+'New.csv'
        fileNameOld = path + ticker+'Old.csv'

        url = 'http://api.marketstack.com/v1/eod?access_key=9addd78f005babaf0124d7d105a5f912&symbols={}'.format(
            ticker)
        print('start retrieving ' + ticker)
        print(url)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                with open(fileNameNew, 'wb') as outfile:
                    outfile.write(r.content)
        except Exception as e:
            print(e.__str__())
        print('finished retrieving ' + ticker)

        print('creating old file')
        # create old file if not exists
        if not os.path.isfile(fileNameOld):
            fold = open(fileNameOld, "wb")
            fold.write(
                "open,high,low,close,volume,adj_high,adj_low,adj_close,adj_open,adj_volume,split_factor,symbol,exchange,date\n")
            fold.close()

        # find difference between old and new file
        # taking difference between old and new file
        with open(fileNameNew, 'r+') as f1:
            lineset = set(f1)
            print(lineset)
            with open(fileNameOld, 'r+') as f2:
                lineset.difference_update(f2)

                print('moving new file to old file')
                cmdMove = ("mv %s %s" % (fileNameNew, fileNameOld))
                os.system(cmdMove)

                print('start writing to Kafka...')
                print(lineset)
                # with open(fileNameTmp, "r") as fileTmp:
                for lineT in lineset:
                    line = lineT.split(',')
                    print(len(line))
                    if len(line) == 14:  # check for correctness
                        line[13] = dt.datetime.strptime(
                            line[13], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                        newLine = [str(time.time()), ticker]
                        transformedLine = ','.join(
                            newLine) + ','+','.join(line)
                        print(transformedLine)
                        producer.send(topicName, transformedLine)
                print('end writing to Kafka...')


if __name__ == "__main__":
    doWork(sys.argv[1], sys.argv[2])
