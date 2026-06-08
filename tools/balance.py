from web3 import Web3

RPC = "https://sepolia.infura.io/v3/YOUR_KEY"

w3 = Web3(Web3.HTTPProvider(RPC))

def get_balance(address):
    balance = w3.eth.get_balance(address)

    return {
        "address": address,
        "eth": w3.from_wei(balance, "ether")
    }
