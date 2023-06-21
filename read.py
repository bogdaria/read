import os

def read_contracts(filename):
    with open(filename, "r") as file:
        contracts = json.load(file)
    return contracts

contracts = read_contracts("contracts.json")

networks = [
    {
        "name": network_name,
        "provider": contracts[network_name]["provider"],
        "base_currency": contracts[network_name]["base_currency"],
        "tokens": contracts[network_name]["tokens"]
    }
    for network_name in contracts
]
