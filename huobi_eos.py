# coding=utf-8
import ccxt
import requests
import pandas as pd
pd.set_option('expand_frame_repr',False)
pd.set_option('display.max_rows',1000)

#huobipro = ccxt.huobipro()
#print(huobipro.id, huobipro.load_markets())
site_base = "https://api.huobi.pro"
site_currency = "/v1/common/symbols"
url = site_base + site_currency
resp = requests.get(url)
print(resp.json()['data'])
# kline
url = site_base + "/market/history/kline" + "?" + "symbol=eosusdt" + "&" + "period=4hour" + "&" + "size=100"
resp = requests.get(url)
print(resp.json())
df = pd.DataFrame(resp.json()['data'])
print(df)

#ticker
url = site_base + "/market/detail/merged" + "?" + "symbol=eosusdt"
resp = requests.get(url)
ticker = resp.json()['tick']
print(ticker['ask'])
print(ticker['bid'])
