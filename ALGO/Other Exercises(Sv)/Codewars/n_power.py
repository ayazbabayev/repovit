# Complete the function that takes a non-negative integer n as input,
# and returns a list of all the powers of 2 with the exponent
# ranging from 0 to n ( inclusive ).

# Examples
# n = 0  ==> [1]        # [2^0]             # base * i
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]


def new_power(number):
    base = 2
    i = 0
    power_result = []
    while i <= number:
        power_result.append(base ** i)
        i += 1
    return power_result

result = new_power(2)
print(result)


# def n_power(n):
#     base = 2
#     i = 0
#     result = []
#
#     while i <= n:
#         result.append(base ** i)
#         i += 1
#
#     return result
#
# test = n_power(3)
# print(test)
#
#
# def n_power2(n):
#     base = 2
#     i = 0
#     result = []
#
#     for i in range(n + 1):
#         result.append(base ** i)
#
#     return result
#
# test2 = n_power2(4)
# print(test2)


# def n_power(number):
#     n_pw = 0
#     power_result = [1]
#     while n_pw >= 0:
#         n_pw +=1
#         print('Power: ',n_pw)
#         power_result.append(number ** n_pw)   # 2 power 3 = 2*0 = 1 / 2*1 = 2 / 2*2 = 4 / 2*2*2 = 8
#         if n_pw == number:
#             break
#     return power_result
#
# number = 3
# result = n_power(number)
# print(result)
