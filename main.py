# The ultimate goal of this project is to create a mixer that can be used to
# Recieve amount in a random wallet in the mixer
# Then trying to get that amount to output wallets X, Y, Z
#
# Inputs: csv file with wallet data, number of wallets to use, input wallet, target wallets

# Our mixer constantly 100 times (can loop infinitely)
# Once a transaction is recieved, it is added to the queue
# Once at the top of the queue, it is processed

import pandas as pd
from scripts import mixer, wallet, functions

def main():
    mixer1 = mixer.Mixer(0, 50)
    mixer2 = mixer.Mixer(0, 50)

    wallet_data = pd.read_csv('data/wallet_data.csv')

    wallets_for_mixer1 = wallet_data.sample(n=1000)

    target_wallets = []

    input_wallet = input("What is the wallet ID you will be transferring from: ")
    input_amount, current_amount = functions.input_amounts()
    target_wallets = functions.input_target_wallets()

    pulling_wallet = wallet.Wallet(input_wallet, current_amount)

    for _, row in wallets_for_mixer1.iterrows():
        mixer1.add_wallet(wallet.Wallet(row['ID'], row['VALUE']))

    count = 0

    while True:
        if count == 100:
            return False
        mixer1.run()
        count += 1


if __name__ == '__main__':
    main()