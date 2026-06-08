from eth_account import Account

class SafeWallet:

    def __init__(self):
        self.account = Account.create()

    def address(self):
        return self.account.address

    def sign(self, tx):
        return Account.sign_transaction(tx, self.account.key)
