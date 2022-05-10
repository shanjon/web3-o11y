# web3-docker

use this repository to spin up a container that pulls data directly from Ethereum using Infura and Web3.py library. the data is then posted as custom events to the New Relic Metric API for querying and visualization.

> Web3.py is a Python library for interacting with Ethereum: https://web3py.readthedocs.io/en/stable/ <br>
> Infura is a service that provides a remote Ethereum node for free - _no $$$ for my own node :')_

## getting started
1. update the `infra_url` parameter in `app.py` with your own Infura API - you can create a free account and API key [here](https://infura.io/register)
2. update the `account_id` and `insert_api_key` parameters with your New Relic account number and Insert API Key

## run locally
you can run this locally on your machine <br>
`docker build [OPTIONS] PATH | URL | -` (i.e., `docker build -t web3-repo .`)

**BUT**❗

## run as ECS task
I wanted to set it up as a scheduled task with ECS to generate a continual flow of Ethereum data to my New Relic dashboards:
1. create Elastic Container Repository to store image  
`aws ecr create-repository --repository-name web3-repo --region region`


2. tag the image with your `repositoryUri`  
`docker tag web3-image aws_account_id.dkr.ecr.region.amazonaws.com/web3-repo`


3. run the `aws ecr get-login-password` command  
`aws ecr get-login-password | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com`


4. push the image to Amazon ECR with the repositoryUri value from the earlier step.
`docker push aws_account_id.dkr.ecr.region.amazonaws.com/web3-repo`


from there you can set up an EventBridge rule to run as a scheduled task (i.e., like a cronjob, run at certain times or intervals as desired)


## review data via NRQL queries and dashboard
this will generate the following custom events:
- `walletBalance`: contains the `balance` of wallets held by Snoop Dogg, Paris Hilton, Lindsay Lohan, Mark Cuban, and Serena Williams
- `blockStatz`: contains the `difficulty`, `gasLimit`, `gasUsed`, `miner`, `number`, and `size` of latest block mined
- `gasPrice`: contains the current `price` or fee per transaction on Ethereum in wei - _one ether = 1,000,000,000,000,000,000 wei (10^18)_

### NRQL example queries
``SELECT * FROM walletBalance`` <br>
``SELECT * FROM blockStatz`` <br>
``SELECT * FROM gasPrice`` <br>


### dashboard
find and replace the `accountId` parameter in the `dashboard.json` file and then import the json to New Relic to use this example dashboard
<img width="954" alt="image" src="https://user-images.githubusercontent.com/68360819/167527943-ada11443-c66c-4c23-9420-bcc647dfb19c.png">
