'''
Created on 21 mai 2017

@author: buissondiaz
'''
from itertools import count
import datetime
if __name__ == '__main__':
    pass

import numpy
import talib
import requests

url = 'https://bleutrade.com/api/v2/public/getcandles?market=MONA_BTC&period=8h&lasthours=724&count=999999'

item= requests.get(url).json()
myList=[]
myList2=[]
counter=0
for price in item['result']:
    myList.append(float(price['Close']))
    data = {}
    data["timestamp"]= datetime.datetime.strptime(price['TimeStamp'], "%Y-%m-%d %H:%M:%S");
    data["volume"]= price['Volume'];
    data["high"]= price['High'];
    data["low"]= price['Low'];
    data["close"]= price['Close'];
    data["open"]= price['Open'];
    data["baseVolume"]= price['BaseVolume'];
    
    
    myList2.append(data)
    print price
    counter=counter+1
print "eee"    
print myList2

print "eee"    
print myList2
import pickle
import os.path
loadd=[]
if os.path.isfile("save.p") :
    loadd = pickle.load( open( "save.p", "rb" ) )
mergedlist = loadd + myList2
myList2=sorted(
    mergedlist,
    key=lambda x: x['timestamp'], reverse=False
)
myList3=[]
keys=set()
for k in myList2:
        if k['timestamp'] not in keys:
            keys.add(k['timestamp'])
            myList3.append(k)
pickle.dump( myList3, open( "save.p", "wb" ) )
close = numpy.random.random(100)
close = numpy.array(myList)
output = talib.SMA(close)

SMA_FAST = 5
SMA_SLOW = 20
MAX_PROFIT = 5
STOP_LOSS = -1
RSI_PERIOD = 10
analysissma_f = talib.SMA(close, SMA_FAST)
analysissma_s = talib.SMA(close, SMA_SLOW)
analysisrsi = talib.RSI(close,RSI_PERIOD)
macd, signal, hist = talib.MACD(close, 
                                    fastperiod=12, 
                                    slowperiod=26, 
                                    signalperiod=9)
print output
print analysisrsi
print macd
print hist
import csv
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(close)
    spamwriter.writerow(output)
    spamwriter.writerow(analysissma_f)
    spamwriter.writerow(analysissma_s)
    spamwriter.writerow(analysisrsi)
    spamwriter.writerow(macd)
    spamwriter.writerow(signal)
    spamwriter.writerow(hist)
    
print myList3
print myList3.__sizeof__()
print myList2.__sizeof__()
