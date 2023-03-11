import time
import random
def mix(mixer, transfer_amount, input_wallet, target_wallets, drop_rate = 0.9):
    dropped_transfer_amount = transfer_amount * drop_rate
    print("You have accepted a {} commission rate".format(1-drop_rate))
    print("You are Mixing {}".format(transfer_amount))
    print("You will receive {}".format(dropped_transfer_amount))
    print("The output will be to the following wallets...")
    print("\n")
    for wallet in target_wallets:
        print("{}:current amount {}".format(wallet.get_identification(), wallet.get_current_value()))
    print("\n")


    start_in = input_wallet.get_current_value()

    while start_in - transfer_amount < input_wallet.get_current_value():
        input_to_mixer = random.sample(mixer.get_wallets(), 1)
        for wallet in input_to_mixer:
            input_wallet.send(wallet)
        print("Amount in Mixer: {}".format(start_in - input_wallet.get_current_value()))


    print("\n")


    time.sleep(2.5)

    mix_iteration = 0
    amount_in_targets = 0
    while dropped_transfer_amount > amount_in_targets:
        mixer.run()
        mix_iteration += 1
        if random.random() <= 0.01:
            print("There have been {} mix cycles".format(mix_iteration))
            target_wallet = random.choice(target_wallets)
            mixer_wallet_output = random.choice(mixer.get_wallets())

            mixer_wallet_output.send(target_wallet)

            amount_in_targets = sum(wallet.get_current_value() for wallet in target_wallets)

            for wallet in target_wallets:
                print("{}: {}".format(wallet.get_identification(), wallet.get_current_value()))
            print("\n")

            # select random amounts to target with preference for low
            # select wallet(s) from mixer
            # send money


