from ape import accounts, project
from datetime import datetime
def main(): 
    contract_name = input("enter contract name: ")
      # Initialize deployer account and print balance 
    #dev_account = accounts.load("scrollsep") 
    dev_account = accounts.load("anvil0") 
    
    print(f'The account balance is: {dev_account.balance / 1e18} ETH')  
     # Deploy the smart contract and print a message 
    # kw = {
    #     'type': 0
    # }
    contract_class = getattr(project, contract_name)

    #deployed_contract = dev_account.deploy(contract_class, **kw, publish=True)
    deployed_contract = dev_account.deploy(contract_class)
    
    print("Contract deployed!") 
    contract_address = deployed_contract.address

    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the contract name, address, and timestamp to a file
    with open("deployed_contracts.txt", "a") as file:
        file.write(f"{current_time}: {contract_name} - Address: {contract_address}\n")

    print(f"{contract_name} address {contract_address} recorded with timestamp.")





# from ape import accounts, project

# def main(): 
#       # Initialize deployer account and print balance 
#     dev_account = accounts.load("scrollsep") 
#     print(f'The account balance is: {dev_account.balance / 1e18} ETH')  
#      # Deploy the smart contract and print a message 
#     kw = {
#         'type': 0
#     }
#     dev_account.deploy(project.hello, **kw) 
#     print("Contract deployed!") 