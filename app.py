from web3 import Web3
import requests

# Infura credentials used to simulate accessing a node
infura_url = "XXXXXXXXXXXXXXXXXXXXX"
web3 = Web3(Web3.HTTPProvider(infura_url))

# New Relic Account ID and API Key
account_id = XXXXXXX
insert_api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Confirm connection to web3
print(web3.isConnected())

# Get whale balances
snoop_balance = web3.eth.getBalance("0xCe90a7949bb78892F159F428D0dC23a8E3584d75")
paris_balance = web3.eth.getBalance("0xB6Aa5a1AA37a4195725cDF1576dc741d359b56bd")
serena_balance = web3.eth.getBalance("0x0864224F3cC570AB909EBF619f7583EF4a50b826")
lohan_balance = web3.eth.getBalance("0x3781d92e5449b5b689fEe308ded44882085b6312")
cuban_balance = web3.eth.getBalance("0xa679c6154b8d4619Af9F83f0bF9a13A680e01eCf")

# POST request to Events API for whale balances
headers = {'X-Insert-Key': insert_api_key, 'Content-Type': 'application/json'}
payload = {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'ParisHilton','balance':paris_balance/1000000000000000000}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'SnoopDogg', 'balance':snoop_balance}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'SerenaWilliams', 'balance':serena_balance/1000000000000000000}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'LindsayLohan', 'balance':lohan_balance/1000000000000000000}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'MarkCuban', 'balance':cuban_balance/1000000000000000000},

r = requests.post("https://insights-collector.newrelic.com/v1/accounts/{account_id}/events", json=payload, headers=headers)

# Get latest block stats
block = web3.eth.get_block('latest')

# POST request to Events API for whale balances
headers = {'X-Insert-Key': insert_api_key, 'Content-Type': 'application/json'}

payload = {
    "eventType": "blockStatz",
    'difficulty': block.difficulty,
    'gasLimit': block.gasLimit,
    'gasUsed': block.gasUsed,
    'miner': block.miner,
    'number': block.number,
    'size': block.size,
    'uncles': block.uncles,
}

r = requests.post("https://insights-collector.newrelic.com/v1/accounts/{account_id}/events", json=payload, headers=headers)

## get gasPrice in Wei
gasPrice = web3.eth.gas_price

# POST request to Events API for gas price
headers = {'X-Insert-Key': insert_api_key, 'Content-Type': 'application/json'}
payload = {'eventType':'gasPrice', 'currency':'Wei', 'price':gasPrice}

r = requests.post("https://insights-collector.newrelic.com/v1/accounts/{account_id}/events", json=payload, headers=headers)


print('success')
