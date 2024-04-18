from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

infura_url = f"https://ropsten.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"
web3 = Web3(Web3.HTTPProvider(infura_url))

def get_balance(address):
    return web3.eth.get_balance(address)

# Example to interact with a contract
# You will need to replace 'CONTRACT_ADDRESS' and 'ABI' with actual contract details
contract_address = Web3.toChecksumAddress('CONTRACT_ADDRESS')
contract_abi = 'ABI'  # ABI for the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def read_contract_data():
    # Example call to a contract's function
    return contract.functions.someFunction().call()
