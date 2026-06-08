from eth_account import Account

def create_wallet():
    acct = Account.create()

    return {
        "address": acct.address,
        "private_key": acct.key.hex()
    }
