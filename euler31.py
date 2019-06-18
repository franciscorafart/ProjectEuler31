# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

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

def coin_combination:


PENCE_VALUE_MAPPING = {
    '0': 1,
    '1': 2,
    '2': 5,
    '3': 10,
    '4': 20,
    '5': 50,
    '6': 100,
    '7': 200,
}
