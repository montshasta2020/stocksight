import os
import time
import configparser


config = configparser.ConfigParser()
config.readfp(open('changes.txt'))
stock_name = config.get('settings', 'stock_name')
keywords_to_search = config.get('settings', 'keywords_to_search')

command_price = "python stockprice.py -s "+ stock_name +" --debug"

print(command_price)

flag = True

while True:
	try:
		if flag == True:
			os.system(command_price)
			flag = False
	except:
		flag = True
