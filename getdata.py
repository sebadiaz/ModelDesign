'''
Created on 21 mai 2017

@author: buissondiaz
'''
from itertools import count
import datetime
import numpy
import requests
import schedule
import time
import sys

moneys = [
    "ADC_BTC",
    "ADC_DOGE",
    "BITB_BTC",
    "BITB_DOGE",
    "BLK_BTC",
    "BLK_DOGE",
    "BSTY_BTC",
    "BSTY_DOGE",
    "BTA_BTC",
    "BTA_DOGE",
    "BTCD_BTC",
    "BTCD_DOGE",
    "CANN_BTC",
    "CANN_DOGE",
    "CDN_BTC",
    "CDN_DOGE",
    "CLAM_BTC",
    "CLAM_DOGE",
    "DASH_BTC",
    "DASH_DOGE",
    "DCR_BTC",
    "DCR_DOGE",
    "DGC_BTC",
    "DGC_DOGE",
    "DOGE_BTC",
    "DP_BTC",
    "DP_DOGE",
    "EFL_BTC",
    "EFL_DOGE",
    "ERC3_BTC",
    "ERC3_DOGE",
    "ETH_BTC",
    "ETH_DOGE",
    "EXP_BTC",
    "EXP_DOGE",
    "FJC_BTC",
    "FJC_DOGE",
    "GB_BTC",
    "GB_DOGE",
    "HTML5_BTC",
    "HTML5_DOGE",
    "LTC_BTC",
    "MNM_BTC",
    "MNM_DOGE",
    "MONA_BTC",
    "MONA_DOGE",
    "MOON_BTC",
    "MOON_DOGE",
    "MUE_BTC",
    "MUE_DOGE",
    "MXT_BTC",
    "MXT_DOGE",
    "NEOS_BTC",
    "NEOS_DOGE",
    "NLG_BTC",
    "NLG_DOGE",
    "NMC_BTC",
    "NMC_DOGE",
    "NVC_BTC",
    "NVC_DOGE",
    "OK_BTC",
    "OK_DOGE",
    "POT_BTC",
    "POT_DOGE",
    "PPC_BTC",
    "PPC_DOGE",
    "RDD_BTC",
    "RDD_DOGE",
    "SLG_BTC",
    "SLG_DOGE",
    "SLR_BTC",
    "SLR_DOGE",
    "SMC_BTC",
    "SMC_DOGE",
    "START_BTC",
    "START_DOGE",
    "SWIFT_BTC",
    "SWIFT_DOGE",
    "TROLL_BTC",
    "TROLL_DOGE",
    "UNO_BTC",
    "UNO_DOGE",
    "VRC_BTC",
    "VRC_DOGE",
    "VTC_BTC",
    "VTC_DOGE",
    "WDC_BTC",
    "WDC_DOGE",
    "XPM_BTC",
    "XPM_DOGE",
    "XVP_BTC",
    "XVP_DOGE",
    "ZET_BTC",
    "ZET_DOGE"
]

def job():
  for money in moneys:
    filename=money+"_save.p"
    url = 'https://bleutrade.com/api/v2/public/getcandles?market='+money+'&period=4h&lasthours=724&count=999999'

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
	counter=counter+1
    import pickle
    import os.path
    loadd=[]
    if os.path.isfile(filename) :
	loadd = pickle.load( open( filename, "rb" ) )
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
    pickle.dump( myList3, open( filename, "wb" ) )
    close = numpy.random.random(100)
    close = numpy.array(myList)
    print len(myList3)
    print len(myList2)
    print money+" clean:"+str(myList3.__sizeof__())
    print money+" previous:"+str(myList2.__sizeof__())

schedule.every(4).hours.do(job)
job()
print "first  job"
while True:
    schedule.run_pending()
    sys.stdout.write('.')
    time.sleep(1)
