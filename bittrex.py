import requests

market = "eth"
jvalues = ("MarketName", "High", "Low", "Volume", "Last", "BaseVolume", "TimeStamp", "Bid", "Ask", "OpenBuyOrders", "OpenSellOrders", "PrevDay", "Created")

def get_json():
    return requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-" + market).json()

def get_update():
    jso = get_json()
    data = []
    for x in xrange(0, len(jvalues)):
        data.append(jso["result"][0][jvalues[x]])
    data = map(str, data)
    return data

def get_value(val, js = get_update()):
    for x in xrange(0, len(jvalues)):
        if val.lower() in jvalues[x].lower():
            if js[x].isdigit():
                return float(js[x])
            else:
                return js[x]

