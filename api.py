import requests

api_key = input('Api key --> ')
s = input('Service --> ')


buy_url = 'http://cheapsms.pro/stubs/handler_api.php?api_key={}&action=getNumber&service={}'.format(api_key, s)
change_url = 'http://cheapsms.pro/stubs/handler_api.php'
balance_url = 'http://cheapsms.pro/stubs/handler_api.php?api_key={}&action=getBalance'.format(api_key)

def getNumber():
	ids = []
	id = requests.get(buy_url).text.split(':')[1]
	return id

	
def setStatuses(ids):
	for i in ids:
		params = {
			'api_key':api_key,
			'action':'setStatus',
			'status':'-1',
			'id':i}
		r = requests.get(change_url, params=params)


def getBalance():
        balance = requests.get(balance_url)
        return balance.text.replace('ACCESS_BALANCE:', '')
    
