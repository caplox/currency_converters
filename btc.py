#!/usr/bin/env python
# Getting BTC price from coindesk using response module
import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
btc_price = data["bpi"]["USD"]["rate"]
f = float(btc_price.replace(',',''))
