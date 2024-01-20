from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

assert w3.is_connected(), 'Failed to connect to the Ethereum client.'

contract_address = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512'
abi = [
    {
        "inputs": [
            {
                "name": "_username",
                "type": "bytes"
            },
            {
                "name": "_favoriteNumber",
                "type": "uint256"
            }
        ],
        "name": "addUser",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_username",
                "type": "bytes"
            }
        ],
        "name": "getFavoriteNumber",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_index",
                "type": "uint256"
            }
        ],
        "name": "getUserNameAtIndex",
        "outputs": [
            {
                "name": "",
                "type": "bytes"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "arg0",
                "type": "bytes"
            }
        ],
        "name": "favoriteNumbers",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "userNames",
        "outputs": [
            {
                "name": "",
                "type": "bytes"
            }
        ],
        "stateMutability": "view",
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

def addUser(_username, _favoriteNumber):
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.addUser(_username, _favoriteNumber).build_transaction({
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

def getFavoriteNumber(_username):
    return contract.functions.getFavoriteNumber(_username).call()

def getUserNameAtIndex(_index):
    return contract.functions.getUserNameAtIndex(_index).call()

def favoriteNumbers(arg0):
    return contract.functions.favoriteNumbers(arg0).call()

def userNames(arg0):
    return contract.functions.userNames(arg0).call()

def userCount():
    return contract.functions.userCount().call()

input_user = 'raza'
addUser(input_user.encode(), 5)
print(getFavoriteNumber(input_user.encode()))