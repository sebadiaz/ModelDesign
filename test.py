'''
Created on 21 mai 2017

@author: buissondiaz
'''
from itertools import count

if __name__ == '__main__':
    pass

import numpy
import talib
import requests

url = 'https://bleutrade.com/api/v2/public/getcandles?market=MONA_BTC&period=8h&lasthours=724&count=999999'

item= requests.get(url).json()
myList=[]
counter=0
for price in item['result']:
    myList.append(float(price['Close']))
    counter=counter+1
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
    
    
