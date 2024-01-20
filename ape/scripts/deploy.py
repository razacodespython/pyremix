from ape import accounts, project
from datetime import datetime
import os
import subprocess

def pyremix(contract):
    contract_name = contract
    subprocess.run(["python", "../pyremix/create_abi.py", contract_name])
    subprocess.run(["python", "../pyremix/createweb3.py"])
    subprocess.run(["python", "../pyremix/create_streamlit_abi.py", contract_name])

    #subprocess.run(["python", "../pyremix/run_setup.py"])

    # Run Streamlit app
    subprocess.run(["streamlit", "run", "streamlit_app.py"])


def main(): 
    contract_name = input("Enter contract name: ")

    # Initialize deployer account and print balance 
    dev_account = accounts.load("anvil0") 
    print(f'The account balance is: {dev_account.balance / 1e18} ETH')  

    # Deploy the smart contract and print a message 
    contract_class = getattr(project, contract_name)
    deployed_contract = dev_account.deploy(contract_class)
    print("Contract deployed!") 
    contract_address = deployed_contract.address

    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the contract name, address, and timestamp to a file
    with open("deployed_contracts.txt", "a") as file:
        file.write(f"{current_time}: {contract_name} - Address: {contract_address}\n")
    print(f"{contract_name} address {contract_address} recorded with timestamp.")

    # Write CONTRACT_ADDRESS to .env file
    env_file_path = "../.env"
    new_lines = []
    contract_address_line = f"CONTRACT_ADDRESS={contract_address}\n"
    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if not line.startswith("CONTRACT_ADDRESS"):
                    new_lines.append(line)
    new_lines.append(contract_address_line)
    with open(env_file_path, "w") as file:
        file.writelines(new_lines)

    # Run 'run_setup.py' in 'pyremix' folder
    pyremix(contract=contract_name)
    




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