# Write code to generate a dictionary where the keys are the numbers from 1 to 50 and the values follow these rules:
# if the number is divisible by 2 the value should be one more than the key
# if the number is divisible by 7 the value should be one less than the key
# if the number is divisible by 2 and 7 the value should be the key multiplied by 2
# otherwise the value should be the same number as the key

numbers = {}
key = 1
value = 1

while key <= 50:
    numbers[key] = value
    key += 1
    value += 1

    if key % 2 == 0 and key % 7 == 0:
        value = key * 2
    elif key % 2 == 0:
        value = key + 1
    elif key % 7 == 0:
        value = key - 1
    else:
        value = key


print(numbers)

# {1: 1, 2: 3, 3: 3, 4: 5, 5: 5, 6: 7, 7: 6, 8: 9, 9: 9, 10: 11, 11: 11, 12: 13, 13: 13,
# 14: 28, 15: 15, 16: 17, 17: 17, 18: 19, 19: 19, 20: 21, 21: 20, 22: 23, 23: 23, 24: 25,
# 25: 25, 26: 27, 27: 27, 28: 56, 29: 29, 30: 31, 31: 31, 32: 33, 33: 33, 34: 35, 35: 34,
# 36: 37, 37: 37, 38: 39, 39: 39, 40: 41, 41: 41, 42: 84, 43: 43, 44: 45, 45: 45, 46: 47,
# 47: 47, 48: 49, 49: 48, 50: 51}
