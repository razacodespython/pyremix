from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

assert w3.is_connected(), 'Failed to connect to the Ethereum client.'

contract_address = '0x5FC8d32690cc91D4c39d9d3abcBD16989F875707'
abi = [
    {
        "inputs": [],
        "name": "addcount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "userCount",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=abi)

account_address = '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
private_key = os.getenv('PRIVATE_KEY')
assert private_key, 'Private key not found in .env file'

def addcount():
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.addcount().build_transaction({
        'chainId': 31337,
        'gas': 2000000,
        'nonce': updated_nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def userCount():
    return contract.functions.userCount().call()

