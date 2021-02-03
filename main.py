import os
import time
import configparser


config = configparser.ConfigParser()
config.readfp(open('changes.txt'))

stock_name = config.get('settings', 'stock_name')
keywords_to_search = config.get('settings', 'keywords_to_search')

mine_url = config.get('settings', 'mine_url')
followlinks = config.get('settings', 'followlinks')
twitteruserids = config.get('settings', 'twitteruserids')


if followlinks.lower() == 'true':
	command_stock = "python sentiment.py -s " + stock_name + " --followlinks --debug"
elif twitteruserids.lower() == 'true':
	command_stock = "python sentiment.py -s " + stock_name + " -f " + " twitteruserids.txt --debug"
elif mine_url.lower() == 'true':
	command_stock = "python sentiment.py -s " + stock_name + " -k " + keywords_to_search + " -l --debug"
else:
	command_stock = "python sentiment.py -s " + stock_name + " -k " + keywords_to_search + " --debug"

print(command_stock)


while True:

	print("\n ************ RUNNING IN LOOP FLAG = *********")
	os.system(command_stock)

