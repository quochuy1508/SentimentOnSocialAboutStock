import csv
import os


def cashtagSet(Type):
    # map the inputs to the function blocks
    flag = 0

    cwd = os.getcwd()
    # define the function blocks
    if Type=="DOW30":
        FILE_NAME = cwd + '/Kafka/data/nasdaq100.csv'
    elif Type=="NASDAQ100":
        FILE_NAME = cwd + '/Kafka/data/nasdaq100.csv'
    elif Type== "NYSE100":
        FILE_NAME = cwd + '/Kafka/data/nyse100.csv'
    elif Type== "SP500":
        FILE_NAME = cwd + '/Kafka/data/SP500.csv'
    elif Type== "NASDAQ_COMPOSITE":
        FILE_NAME = cwd + '/Kafka/data/NASDAQComposite.csv'
    elif Type== "NYSE_COMPOSITE":
        FILE_NAME = cwd + '/Kafka/data/NYSEComposite.csv'        
    elif Type== "COMPANIES":
        FILE_NAME = cwd + '/Kafka/data/companies.csv'        
    elif Type== "ALL":
        FILE_NAME = cwd + '/Kafka/data/allStocks.csv'
        flag = 1
    else:
        raise Exception("unknown stock type")
        
    with open(FILE_NAME,'rU') as file1:
        if flag==1:
            dat = csv.reader(file1,  dialect=csv.excel_tab, delimiter=',')
            idx = 1
        else:
            dat = csv.reader(file1, dialect=csv.excel_tab, delimiter=',')
            next(dat, None) 
            idx = 0
        
        filterTwitter = set()
        for line in dat:
            filterTwitter.add('$'+line[idx])
        
        return filterTwitter
