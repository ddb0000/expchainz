import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

infura_url = f"https://sepolia.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"
web3 = Web3(Web3.HTTPProvider(infura_url))

with open('contract_abi.json', 'r') as abi_definition:
    contract_abi = json.load(abi_definition)

contract_address = Web3.to_checksum_address(os.getenv('CONTRACT_ADDRESS'))
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def get_token_balance(address):
    balance_wei = contract.functions.balanceOf(address).call()
    balance_eth = Web3.from_wei(balance_wei, 'ether')
    return balance_eth

def read_contract_data():
    return contract.functions.totalSupply().call()
