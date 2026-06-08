from web3 import Web3

RPC = "https://sepolia.infura.io/v3/YOUR_KEY"
w3 = Web3(Web3.HTTPProvider(RPC))

def send_eth(data: dict):
    """
    data = {
        "from": "",
        "private_key": "",
        "to": "",
        "amount": 0.01
    }
    """

    nonce = w3.eth.get_transaction_count(data["from"])

    tx = {
        "nonce": nonce,
        "to": data["to"],
        "value": w3.to_wei(data["amount"], "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei("10", "gwei"),
    }

    signed = w3.eth.account.sign_transaction(tx, data["private_key"])
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)

    return {
        "tx_hash": tx_hash.hex()
    }
