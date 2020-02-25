from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json

	# Grab Crypto Price 
	url1 = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRXs&tsyms=USD"
	key = "5d4f2c346f7b28e26b158aa6ed035635b284de696d2e3c9e3417b96059474cc7"
	url = url1+'&api_key='+key

	price_request = requests.get(url)
	price = json.loads(price_request.content)

	# Grab Crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api':api, 'price':price})


def prices(request):

	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['check']
		quote = quote.upper()
		url1 = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD"
		key = "5d4f2c346f7b28e26b158aa6ed035635b284de696d2e3c9e3417b96059474cc7"
		url = url1+'&api_key='+key
		crypto_request = requests.get(url)
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'crypto':crypto})
	
	else:
		notfound = """Enter a crypto symbol.."""
		return render(request, 'prices.html', {'notfound':notfound})