import random
from scripts import wallet
def split_list(lst):
    random.shuffle(lst)  # Shuffle the original list randomly
    mid = len(lst) // 2  # Calculate the middle index of the shuffled list
    return lst[:mid], lst[mid:]


def check_lists(list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            print("Error")
            list1.remove(list1[i])
            list2.remove(list2[i])

            list1, list2 = check_lists(list1, list2)
            return list1, list2

    return list1, list2

def update_wallets_in_mixer(mixer1, mixer2):
    all_wallets = []

    all_wallets.extend(mixer1.wallets)
    all_wallets.extend(mixer2.wallets)

    mixer1.wallets, mixer2.wallets = split_list(all_wallets)

    return mixer1.wallets, mixer2.wallets

def input_target_wallets():
    list_of_target_wallets = []
    break_point = False

    while break_point is False:
        new_wallet = input("Please enter a target wallet: ")
        list_of_target_wallets.append(wallet.Wallet(new_wallet, 0))

        if len(list_of_target_wallets) < 3:
            print("Please add more target wallets for security")
        else:
            add_another = input("Would you like to enter another wallet [y/n]: ")

            if add_another == "n":
                break_point = True


    return list_of_target_wallets


def input_amounts():
    value_check = False
    while value_check is False:
        input_amount = input("What is the amoount you would like to Mix: ")
        current_amount = input("How much do you currently have in that wallet: ")

        if input_amount > current_amount:
            print("You do not have enough in your wallet to Mix")

        else:
            value_check = True

    return input_amount, current_amount