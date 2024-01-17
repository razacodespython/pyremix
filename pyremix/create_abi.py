import json
import os

def write_abi_to_env(contract_name):
    # Adjust file path to point to the correct location
    file_path = os.path.join("..", "ape", ".build", f"{contract_name}.json")

    # Read ABI from the JSON file
    try:
        with open(file_path, 'r') as file:
            contract_data = json.load(file)
            abi = contract_data['abi']
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return
    except KeyError:
        print(f"ABI not found in {file_path}.")
        return

    # Adjust .env file path to be at the same level as pyremix folder
    env_file_path = os.path.join("..", ".env")
    abi_str = json.dumps(abi)
    
    # Check if .env file exists, and create if it doesn't
    if not os.path.exists(env_file_path):
        with open(env_file_path, 'w') as file:
            file.write("")

    with open(env_file_path, 'a') as file:
        file.write(f"ABI={abi_str}\n")

    print("ABI written to .env file.")

# Example usage
contract_name = input("Enter the contract name: ")
write_abi_to_env(contract_name)
