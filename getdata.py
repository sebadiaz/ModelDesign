'''
Created on 24 mai 2017

@author: buissondiaz
'''
import pickle
import numpy
import talib
import os
import math
import csv
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

for money in moneys:
    filename=money+"_save.p"
    loadd=[]
    if os.path.isfile(filename) :
     openfile = open( filename, "rb" )
     try:
      loadd = pickle.load( openfile )
     except IOError as e:
      print "Error on "+money +" "+e
      continue 
     closeIn=[]
     highIn=[]
     lowIn=[]
     openIn=[]
     volumeIn=[]
     for loa in loadd:
         closeIn.append(float(loa['close']))
         highIn.append(float(loa['high']))
         lowIn.append(float(loa['low']))
         openIn.append(float(loa['open']))
         volumeIn.append(float(loa['volume']))
     close = numpy.array(closeIn)
     high = numpy.array(highIn)
     low = numpy.array(lowIn)
     openv = numpy.array(openIn)
     volume= numpy.array(volumeIn)
     adx=talib.ADX(high, low, close)
     adxr=talib.ADXR(high, low, close)
     apo=talib.APO(close)
     aroondown, aroonup =talib.AROON(high,low)
     aroonosc=talib.AROONOSC(high,low)
     bop=talib.BOP(openv,high,low,close)
     cci=talib.CCI(high,low,close)
     cmo=talib.CMO(close)
     dx=talib.DX(high,low,close)
     macd, macdsignal, macdhist =talib.MACD(close)
     mfi=talib.MFI(high,low,close,volume)
     minus_di=talib.MINUS_DI(high, low, close)
     #minus_dm=talib.MINUS_DM(high, low, close)
     momentum = talib.MOM(close)
     plus_di=talib.PLUS_DI(high,low,close)
     #plus_dm=talib.PLUS_DM(high,low,close)
     ppo=talib.PPO(close)
     roc=talib.ROC(close)
     rocp=talib.ROCP(close)
     rocr=talib.ROCR(close)
     rocr100=talib.ROCR100(close)
     rsi = talib.RSI(close,10)
     slowk, slowd=talib.STOCH(high,low,close)
     fastk, fastd=talib.STOCHF(high,low,close)
     fastkrsi, fastdrsi=talib.STOCHRSI(close)
     trix=talib.TRIX(close)
     ultosc=talib.ULTOSC(high, low, close)
     willr=talib.WILLR(high, low, close)
     
     for i in range(1,len(loadd)) :
         index=len(loadd)-i
         data=[]
         if close[index-4]==0:
             continue
         datay=(close[index]-close[index-4])/close[index-4]>0.01
         if datay:
             datay=1
         else:
             datay=0
         datadiffadx=adx[index-4]-adx[index-5]
         if math.isnan(datadiffadx):
            continue
         dataadx=adx[index-4]
         datadiffrsi=rsi[index-4]-rsi[index-5]
         datarsi=rsi[index-5]
         datadiffmom=momentum[index-4]-momentum[index-5]
         datamom=momentum[index-5]
         datadiffslowk=slowk[index-4]-slowk[index-5]
         dataslowk=slowk[index-5]
         datadiffwillr=willr[index-4]-willr[index-5]
         datawillr=willr[index-5]
         with open('eggs.csv', 'a') as csvfile:
             spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
             spamwriter.writerow([money, datay, datadiffadx,dataadx,datadiffrsi,datarsi,datadiffmom,datamom,datadiffslowk,dataslowk,datadiffwillr,datawillr])
         
     
