'''
Created on Oct 3, 2020

@author: andrei
'''
from iexfinance.stocks import Stock


# IEX_TOKEN = "pk_1faa5416765b436f9ed2b9ecaf85c85b"
# 
# 
# stock_list = ["ATVI", "ADBE", "AMD", "ALXN", "ALGN", "GOOG", "GOOGL"]
# 
# for i in stock_list:
#     a = Stock(str(i), token = IEX_TOKEN)
#     print(a.get_quote()["latestPrice"])

numbers = input(" Enter four numbers: ")

numberlist = numbers.split(" ")

for i in range(len(numberlist)):
    numberlist[i] = int(numberlist[i])
    
print(numberlist)
