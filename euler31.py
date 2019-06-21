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

def coinBagToNumber(coinBag):
    coin_total = 0
    for index, value in enumerate(coinBag):
        p_amount = PENCE_VALUE_MAPPING[str(index)] or 0
        coin_total+=p_amount*value

    return coin_total

def addsTwo(numbers):
    addition = 0
    for number in numbers:
        addition+=number

    if addition==2:
        return true

    return false

def coin_combination(value, number_of_coins, coin_index = 0, coin_bag= [0,0,0,0,0,0,0,0]):
    reminder = value
    this_coin_bag = coin_bag.copy()

    if reminder == 0 and number_of_coins==0:
        return this_coin_bag

    coin_value = PENCE_VALUE_MAPPING[str(coin_index)]

    if coin_value == reminder and number_of_coins == 1:
        # Fill the bag
        this_coin_bag[coin_index] = coin_bag[coin_index] + 1 # Add one coin on index
        return this_coin_bag

    if coin_value==reminder and number_of_coins>1 and coin_index<7:
        return coin_combination(reminder, number_of_coins, coin_index+1, this_coin_bag)

    if coin_value>reminder and number_of_coins>1 and coin_index<7:
        return coin_combination(reminder, number_of_coins, coin_index+1, this_coin_bag)

    if coin_value < reminder and number_of_coins>0:
        this_coin_bag[coin_index] = coin_bag[coin_index] + 1 # Fill the bag
        reminder = reminder-coin_value # substract coin amount
        return coin_combination(reminder, number_of_coins-1, coin_index, this_coin_bag)

    # returns the coin combination as an array or None
    return None

# We know whe maximum amount of coins is 200
result = 0
for i in range(5):
    combination = coin_combination(200, i+1)
    coin_addition = 0
    if combination is not None:
        coin_addition = coinBagToNumber(combination)
    print ('combination: {} for {} coins, adds: {}'.format(combination, i+1, coin_addition))
    if combination:
        result+=1


# Idea 2
# with 102 coins combination is 100x1p & 2x50p
# with 90 coins (90/200 == 2.22) (78*2p)156 + 27()+ (10p 5p 2p) 17
# Divide 200 in the number of coins (ex. 200/102 coins == 1.9)
    # If division is one of our coins fill bag with that one, if not pick the
    # value that follows our division downwards

# Idea 3
#
