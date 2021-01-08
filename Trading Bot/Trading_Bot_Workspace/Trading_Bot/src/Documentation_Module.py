'''
Created on Sep 16, 2020

@author: Andrei Secara

Module to document everything that the bot does.
'''

def write_original_stock_list(stocks_to_monitor, stock_list_file):
    for i in range(len(stocks_to_monitor)):
        stock_list_file.write(str(stocks_to_monitor[i])+"\n")
        
