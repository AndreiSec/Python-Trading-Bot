'''
Created on Sep 16, 2020

@author: Andrei Secara

Trading algorithm bot version 1
'''

#PYTHON IMPORTS
# import yfinance as yf
# from yahoofinancials import YahooFinancials
# import pandas as pd

from datetime import date, timedelta, datetime

import time

import math

import os #FOR FILES 

import sys # FOR CONSOLE OUTPUT

from openpyxl import Workbook #EXCEL PACKAGE

#MODULE IMPORTS
from Account_Module import *

from Excel_Module import *

from Documentation_Module import write_original_stock_list

from Time_Module import time_checker, get_time, get_date

from Stock_Module import *

from Email_Module import send_email
### TEST


#To record console output to file
sys.stdout = open('Console_output.txt', 'a')



"""WHEN YOU WANT TO USE REAL MONEY / PAPER TRADING USE THE ALPACA API!!!"""


#Define account as object for later use
# account = account_specifier_defined()


#Excel file inputs
stock_list_file_name_1 = "C:\\Users\\andrei\\Desktop\\Trading Bot\\Information\\Stocks.xlsx"
stock_list_sheet_1 = "Sheet"
# stock_list_file_name_2 = "C:\\Users\\andrei\\Desktop\\Trading Bot\\Information\\TSX_Constituents.xlsx"
# stock_list_sheet_2 = "TSX_Constituents"




# stocks_to_monitor += create_stock_list(stock_list_file_name_2, stock_list_sheet_2)


#Removes duplicates on both the NYSE and TSX
# stocks_to_monitor = list(set(stocks_to_monitor))

#Opens file to write down list 
# stock_list_file = open("Stock_List.txt", "w")

#Write stock list to txt_file for documentation purposes
# write_original_stock_list(stocks_to_monitor, stock_list_file)

def main_loop(stocks_to_monitor_tickers):
    on = 1
    while on == 1:
        sys.stdout = open('Console_output.txt', 'a')
        
         
        open_or_close = time_checker()
#         open_or_close = "Close"
        #SETTINGS INITIAL DATE
        yesterday_date = date.today() - timedelta(days=1)
        today_date = date.today()
        
        
        current_date = str(get_date())
        newdir = str('C:\\Users\\andrei\\Desktop\\Trading Bot\\ARCHIVES\\Archive File '+ current_date)
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        
        
        if open_or_close == "Open":
            print()
            print("OPEN")
            print(today_date)
#             stock_list_object = create_stock_list_object(stocks_to_monitor)
  
              
            stock_list_object = create_stock_list_object(stocks_to_monitor_tickers)
#             
            workbook = Workbook()
            sheet = workbook.active
#             sheet["A1"] = "Ticker"
#             sheet["A2"] = "Price"
            a = 1
            b = 1
             
            print("Number of stocks in list: " + str(len(stock_list_object)))
             
            for stock in stock_list_object:
#                 print(len(stock_list_object))
#                 if  stock.price != "nan" and stock.price != "":
#                 print(stock.ticker, stock.price, datetime.today())
                sheet[str("A"+str(a))] = stock.ticker
                sheet[str("B"+str(b))] = stock.price
                a+=1
                b+=1
            workbook.save(newdir + '\\Open.xlsx')
            
            today_open_file = "C://Users//andrei//Desktop//Trading Bot//ARCHIVES//Archive File " + str(today_date) + "//Open.xlsx"
            today_ticker_list = create_stock_list(today_open_file, stock_list_sheet_1)
            today_price_list = create_price_list(today_open_file, stock_list_sheet_1)
            today_stock_list_object = create_yesterday_stock_list_object(today_ticker_list, today_price_list)
            
            
            yesterday_close_file = "C://Users//andrei//Desktop//Trading Bot//ARCHIVES//Archive File " + str(yesterday_date) + "//Close.xlsx"
            yesterday_ticker_list = create_stock_list(yesterday_close_file, stock_list_sheet_1)
            yesterday_price_list = create_price_list(yesterday_close_file, stock_list_sheet_1)
#             print(yesterday_price_list)
            yesterday_stock_list_object = create_yesterday_stock_list_object(yesterday_ticker_list, yesterday_price_list)
            
            print("Number of stocks in todays list: " +str(len(today_stock_list_object)))
            print("Number of stocks in yesterdays list: " +str(len(yesterday_stock_list_object)))
            
            
            
            
            stocks_that_opened_5_below = []
            for i in range(len(today_stock_list_object)):
#                 print(today_stock_list_object[i].ticker, today_stock_list_object[i].price, yesterday_stock_list_object[i].price)
#                 print(str(float(today_stock_list_object[i].price)) + "        "+ str(float(yesterday_stock_list_object[i].price)))
                if (float(today_stock_list_object[i].price) <= float(yesterday_stock_list_object[i].price) * 0.95) and float(today_stock_list_object[i].price) != 0:
                    stocks_that_opened_5_below.append(today_stock_list_object[i])
            
            if stocks_that_opened_5_below != []:
                stocks_that_opened_5_below_tickers = []
                for i in range(len(stocks_that_opened_5_below)):
                    stocks_that_opened_5_below_tickers.append(stocks_that_opened_5_below[i].ticker)
                print("Stocks that opened below 5 today: " + str(stocks_that_opened_5_below_tickers))
                send_email(stocks_that_opened_5_below_tickers)

            #Tries to buy and sell the stocks in stocks_that_opened_5_below
            for i in range(len(stocks_that_opened_5_below)):
#                 print(today_stock_list_object[i].ticker, today_stock_list_object[i].price, yesterday_stock_list_object[i].price)
#                 print(str(float(today_stock_list_object[i].price)) + "        "+ str(float(yesterday_stock_list_object[i].price)))
                success = buy_and_sell(stocks_that_opened_5_below[i].ticker, stocks_that_opened_5_below[i].price)
                if success == True:
                    break
                
                
            
            
            
            

        elif open_or_close == "Close":
            print()
            print("CLOSE")
            print(today_date)
            stock_list_object = create_stock_list_object(stocks_to_monitor_tickers)
            workbook = Workbook()
            sheet = workbook.active
#             sheet["A1"] = "Ticker"
#             sheet["A2"] = "Price"
            a = 1
            b = 1
            for stock in stock_list_object:
#                 if stock.price.isnumeric and stock.price != "nan" and stock.price != "":
                print(stock.ticker, stock.price, datetime.today())
                sheet[str("A"+str(a))] = stock.ticker
                sheet[str("B"+str(b))] = stock.price
                a+=1
                b+=1
            workbook.save(newdir + '\\Close.xlsx')
        sys.stdout.close()
#         on = 0 #JUST HERE WHILE TESTING


#A list of stocks that have been manually inputted to monitor. All of these are from the TSX and NYSE.
stocks_to_monitor_tickers = create_stock_list(stock_list_file_name_1, stock_list_sheet_1)


main_loop(stocks_to_monitor_tickers)


    

