from Projects.Other.Finished import btc
import Projects.currency_con.currency_req.cur_rq_v2 as currq

# Currencies with USD as base.
BTC = btc.f
EUR = currq.ex_rate_EUR
USD = float(1)
GBP = currq.ex_rate_GBP
SEK = currq.ex_rate_SEK
DKK = currq.ex_rate_DKK

# Asking input from user for the converting.
currency_request1 = input("What is your first currency? ")
amount = input("How much of this currency do you have? ")
currency_request2 = input("What is your second currency? ")

# All the conversions.
if currency_request1 == "BTC":
    currency1 = BTC

if currency_request1 == "EUR":
    currency1 = EUR

if currency_request1 == "USD":
    currency1 = USD

if currency_request1 == "GBP":
    currency1 = GBP

if currency_request1 == "SEK":
    currency1 = SEK

if currency_request1 == "DKK":
    currency1 = DKK

if currency_request2 == "BTC":
    currency2 = BTC

if currency_request2 == "EUR":
    currency2 = EUR

if currency_request2 == "USD":
    currency2 = USD

if currency_request2 == "GBP":
    currency2 = GBP

if currency_request2 == "SEK":
    currency2 = SEK

if currency_request2 == "DKK":
    currency2 = DKK

# da math
try:
    print(float(amount) * currency1 / currency2, currency_request2)
except NameError:
    print("Error: We don't have this currency in our system yet.")
