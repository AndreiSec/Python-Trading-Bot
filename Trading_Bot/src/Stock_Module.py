'''
Created on Sep 16, 2020

@author: Andrei Secara

Contains the stock class and stock related functions.
'''
# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
# from List_array import List
from datetime import date, timedelta, datetime
import time
import math
from iexfinance.stocks import Stock
from copy import deepcopy

import finnhub


IEX_TOKEN = read("iex_token.txt")
twelve_data_token = read("twelve_data_token.txt")
finnhub_token = read("finnhub_token.txt")
# td = TDClient(apikey = twelve_data_token)  

finnhub_client = finnhub.Client(api_key=finnhub_token)

#Stock Object
class Py_Stock:
    def __init__(self):
        self.ticker = ""
        self.price = 0
    
        
        
#Fills a stock object with data
def create_stock(tickerstr):
    try:
#         print("D")
        stock = Py_Stock()
        tempstock = Stock(str(tickerstr),  token= IEX_TOKEN)
#         print(tempstock)
        
        stock.ticker = str(tickerstr)
        stock.price = tempstock.get_quote()["latestPrice"]
        
#         stock.price = tempstock.get_price(token= IEX_TOKEN)
#         stock.price = finnhub_client.quote(tickerstr)
#         stock.price = float(si.get_live_price(tickerstr))
#         stock.price = stock.price['c']

        
#         print("D")
#         print(str(stock.ticker) + str(stock.price))

#         del tempstock
        
#         stock.price = str(si.get_live_price(str(tickerstr)))
#         print(stock.price)
#         if stock.price.isnumeric:
#             stock.price = int(stock.price)
#             print(stock.ticker, stock.price)
#         else:
#             print("D")
#             stock.price = str("NA")
#         
    except:
        None
    
    return stock
    

def create_stock_with_price(tickerstr, price):
    try:
        stock = Py_Stock()
        stock.ticker = str(tickerstr)
        stock.price = float(price)
#         print(stock.price)
#         if stock.price.isnumeric:
#             stock.price = int(stock.price)
#             print(stock.ticker, stock.price)
#         else:
#             print("D")
#             stock.price = str("NA")
#         
    except:
        None
    
    return stock


#Creates stock objects from list and stores them in a list object.
def create_stock_list_object(stock_list):
    l = []
    stock_list.sort()
#     print(stock_list)
    for i in stock_list:
#         print(i)
        stock_object = create_stock(i)
        try:
#             print(stock_object.price)
#             stock_object.price = float(stock_object.price)
            print(i)

#             stock_object.price = float(si.get_live_price(str(i)))
            if not math.isnan(stock_object.price):
                l.append(stock_object)
        except ValueError:
            None
            
#         print("Length of stock list: " + str(len(l)))
    return l


def create_yesterday_stock_list_object(stock_list, stock_price_list):
    l = []
    for i in range(len(stock_list)):
#         print(i)
        stock_object = create_stock_with_price(stock_list[i], stock_price_list[i])
        try:
            stock_object.price = float(stock_object.price)
            if not math.isnan(stock_object.price):
                l.append(stock_object)
        except ValueError:
            None
            
#         print("Length of stock list: " + str(len(l)))
    return l


def single_stock_price_checker_loop(original_price, ticker):
    seconds_in_30_minutes = 3600
    seconds_elapsed = 0
#     stock_object = create_stock(ticker)
    while seconds_elapsed != seconds_in_30_minutes:
        
#         price = float(stock_object.price)
        price = float(si.get_live_price(str(ticker)))
        if price >= original_price * 1.01 or price <= original_price * 0.99:
            return price
        time.sleep(1)
        seconds_elapsed += 1
        
    return price

