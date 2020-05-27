from oanda_class import kucingJoget, kucingTukang
import json

#x = kucingJoget()
#y = kucingTukang()

#print(y.strToTime('2020-05-21T22:35:00.000000000Z', None))
#print(y.strToTime('2020-05-21T22:35:00.000000000Z', 'utc'))
#print(y.strToTime('2020-05-21T22:35:00.000000000Z', 'local'))

# getInstrumentCandles
d_getInstrumentCandles = {
    'instrument' : 'AUD_USD',
    'count' : '2',
    'price' : 'M',
    'granularity' : 'M5',
    'from' : None
    }
#time = datetime(2020, 5, 21, 21, 5, 0, 0)
#time = datetime.now() - timedelta(days=4)
#time = time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
#d_getInstrumentCandles['from'] = quote(time)
#res = (x.getInstrumentCandles(d_getInstrumentCandles))

res = {'instrument': 'AUD_USD', 'granularity': 'M5', 'candles': [{'complete': True, 'volume': 63, 'time': '2020-05-27T11:10:00.000000000Z', 'mid': {'o': '0.66687', 'h': '0.66697', 'l': '0.66654', 'c': '0.66658'}}, {'complete': True, 'volume': 68, 'time': '2020-05-27T11:15:00.000000000Z', 'mid': {'o': '0.66654', 'h': '0.66658', 'l': '0.66612', 'c': '0.66638'}}, {'complete': True, 'volume': 43, 'time': '2020-05-27T11:20:00.000000000Z', 'mid': {'o': '0.66640', 'h': '0.66640', 'l': '0.66612', 'c': '0.66633'}}, {'complete': True, 'volume': 37, 'time': '2020-05-27T11:25:00.000000000Z', 'mid': {'o': '0.66636', 'h': '0.66674', 'l': '0.66632', 'c': '0.66672'}}, {'complete': False, 'volume': 21, 'time': '2020-05-27T11:30:00.000000000Z', 'mid': {'o': '0.66668', 'h': '0.66668', 'l': '0.66651', 'c': '0.66654'}}]}
{'instrument': 'AUD_USD', 'granularity': 'M5', 'candles': [{'complete': True, 'volume': 37, 'time': '2020-05-27T11:25:00.000000000Z', 'mid': {'o': '0.66636', 'h': '0.66675', 'l': '0.66633', 'c': '0.66672'}}, {'complete': False, 'volume': 21, 'time': '2020-05-27T11:30:00.000000000Z', 'mid': {'o': '0.66668', 'h': '0.66669', 'l': '0.66652', 'c': '0.66654'}}]}


li = []

for candle in res['candles']:
    if candle['complete'] == True:
        data = {}
        data['instrument'] = res.get('instrument')
        data['granularity'] = res.get('granularity')
        data['volume'] = candle['volume']
        data['time'] = candle['time']
        data.update(candle['mid'])
        li.append(data)
    
for l in li:
    print(l)
