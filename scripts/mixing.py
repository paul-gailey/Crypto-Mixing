
def mix(mixer, transfer_amount, input_wallet, target_wallets, drop_rate = 0.9):
    dropped_transfer_amount = transfer_amount * 0.9

    while dropped_transfer_amount != 0:
        for wallet in target_wallets:
            print("{}: {}".format(wallet.get_identification(), wallet.get_current_value()))

        print("\n")


