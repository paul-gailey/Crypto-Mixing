import random
from scripts import functions

class Mixer:
    def __init__(self, current_value=0, limit_transactions=50):
        self.current_value = current_value
        self.run_state = True
        self.wallets = [] # List of wallets, wallet is a class
        self.limit_transactions = limit_transactions

    def update_current_value(self, amount_change, operation):
        if operation == 'add':
            self.current_value += amount_change
        elif operation == 'subtract':
            self.current_value -= amount_change

    def get_current_value(self):
        self.current_value = sum(wallet.current_value for wallet in self.wallets)
        return self.current_value

    def run(self):
        if len(self.wallets) == 0:
            raise ValueError("No wallets in mixer")

        n_transactions = random.randint(0, self.limit_transactions)  # Get random number of transactions -> len(self.wallets)
        random_wallets = random.sample(self.wallets, n_transactions)  # Get random wallets
        target_wallets = random.sample(self.wallets, n_transactions)
        """
        print("{} transactions will be preformed:".format(n_transactions))
        print("{}".format(random_wallets))
        print("{}".format(target_wallets))
        """
        random_wallets, target_wallets = functions.check_lists(random_wallets, target_wallets)

        for i, wallet in enumerate(random_wallets):
            if wallet != target_wallets[i]:
                wallet.send(target_wallets[i])

    def add_wallet(self, wallet):
        self.wallets.append(wallet)
            # Check if there is a transaction in the queue
            # If there is, process it
            # If not, wait




    def stop(self):
        pass


    def get_output(self):
        return self.output

