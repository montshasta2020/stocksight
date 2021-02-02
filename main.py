import os
import time
import configparser


config = configparser.ConfigParser()
config.readfp(open('changes.txt'))
stock_name = config.get('settings', 'stock_name')
keywords_to_search = config.get('settings', 'keywords_to_search')


command_stock = "python sentiment.py -s "+ stock_name + " -k "+ keywords_to_search +" --debug"
command_price = "python stockprice.py -s "+ stock_name +" --debug"

print(command_stock)
print(command_price)

flag = True
gone_excpet = False

while True:

	print("\n ************ RUNNING IN LOOP FLAG = "+ str(flag) + " GONE_EXCPET = "+ str(gone_excpet) + "*********")
	os.system(command_stock)

