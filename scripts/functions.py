import random
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