# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# idea.
# start with one coin and upwards

# case 3
# Pick the largest that is <= to the value
# Pick again. If == 2 break and continue. If larger, start from the next coin all over
# If smaller try picking next coin

# How do we know when a number of coins has reached all its possible combinations?
# There should only be one combination for a determinate number of coins ?

def coin_combination(value, number_of_coins, start_coin_index, coin_bag= [0,0,0,0,0,0,0,0]):

    current_coin_index = start_coin_index

    # Fill the bag
    for i in range(number_of_coins):
        this_coin_bag[current_coin_index]=this_coin_bag[current_coin_index]+1
        bag_total = coinBagToNumber(this_coin_bag)
        if bag_total == 200:
            return this_coin_bag
        if bag_total < 200:
            return # coin_combination(200, number_of_coins)
        if bag_total>200:
            return # coin_combination(200, number_of_coins, )

    # returns the coin combination as an array or None
    return None

# We know whe maximum amount of coins is 200
result = 0
for i in range(200):
    combination = coin_combination(200, i+1, 0)
    if combination:
        result+=1

# Takes array
def coinBagToNumber(coinBag):
    coin_total = 0
    for index, value in coinBag:
        p_amount = PENCE_VALUE_MAPPING[str(index)] or 0
        coint_total+=p_amount*value

    return coin_total

def addsTwo(numbers):
    addition = 0
    for number in numbers:
        addition+=number

    if addition==2:
        return true

    return false


PENCE_VALUE_MAPPING = {
    '7': 1,
    '6': 2,
    '5': 5,
    '4': 10,
    '3': 20,
    '2': 50,
    '1': 100,
    '0': 200,
}
