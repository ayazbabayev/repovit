# # # EVENS AND ODDS!!! # # # count evens odds / count even odd

# def even_function(n):
#     even = 0
#     odd = 0
#     while n != 0:
#         i = n % 10
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#         n = n // 10
#     return [even, odd]
#                                       # Can we print the values of even & odd here?
# test = 12345
# result = even_function(test)
# print(result)
########################################################################################################################
def even_finder(n):
    digit_list = [int(d) for d in str(n)]
    even_nums = []
    odd_nums = []

    for d in digit_list:
        if d % 2 == 0:
            even_nums.append(d)
        else:
            odd_nums.append(d)

    print('evens:',even_nums, ' odds:', odd_nums)
    final_list = []
    for ele in even_nums:           # shorter: even_nums+odd_nums
        final_list.append(ele)      # PS why it gives only odds in 'for ele in even_nums and odd_nums'?
    for ele in odd_nums:
        final_list.append(ele)

    return final_list

test = 12345
result = even_finder(test)
print(result)

# print("Count of the even digits: ", even_count)
# print("Count of the odd digits : ", odd_count)

# def evener(x):
#     evens = 0
#     odds = 0
#     while x != 0:
#         i = x % 10
#         if i % 2 == 0:
#             evens += 1
#         else:
#             odds += 1
#         x = x // 10
#     return [evens, odds]
#
# test = 12345
# result = evener(test)
# print(result)

# def evener(x):
#     digit_list = [int(d) for d in str(x)]
#     even = []
#     odd = []
#     final_list = []
#     for d in digit_list:
#         if d % 2 == 0:
#             even.append(d)
#         else:
#             odd.append(d)
#
#     for d in even + odd:
#         final_list.append(d)
#     return final_list
#
# test = 12345
# result = evener(test)
# print(result)

# def evener1(x):
#     digit_list = [int(d) for d in str(x)]
#     evens =[]
#     odds = []
#
#     for d in digit_list:
#         if d % 2 == 0:
#             evens.append(d)
#         else:
#             odds.append(d)
#
#     total_list = []
#     print('evens:',evens,'odds:', odds)
#     return evens+odds
#
# test = 12345
# result = evener1(test)
# print(result)

#######################################
# def evener2(x):
#     evens= 0
#     odds= 0
#
#     while x != 0:
#         i = x % 10      # !
#         if i % 2 == 0:
#             evens += 1
#         else:
#             odds += 1
#         x = x // 10     # !
#     return ('even count:', evens, 'odd count:', odds)
#
# test = 24568
# result =evener2(test)
# print(result)

# ######################################################################################################################

def evenodder(x):
    evens=[]
    odds=[]
    digit_list = [int(d) for d in str(x)]
    print('dl',digit_list)
    for d in digit_list:
        if d%2==0:
            evens.append(d)
        else:
            odds.append(d)
    return 'e',evens,'o',odds

print(evenodder(x=12345))

########################################################################################################################

def evodder(x):
    ev=0
    od=0
    while x != 0:
        d = x % 10
        if d%2==0:
            ev+=1
        else:
            od+=1
        x=x//10
    return ev,od
print(evodder(x=123456789))


def evodder2(x):
    ev=[]
    od=[]
    digit_list=[int(d) for d in str(x)]
    for d in digit_list:
        if d%2==0:
            ev.append(d)
        else:
            od.append(d)
    return ev,od
print(evodder2(x=123456789))


########################################################################################################################
# def find_min_num(num_div):
#     div_list=[]
#     no = num_div
#
#     while num_div != 0:
#
#         num_div / no
#         print(f'{num_div}/{no}:',num_div/no)
#
#         if num_div % no == 0:
#             div_list.append(no)
#             print('YES!')
#             print(div_list)
#
#         no-=1
#
#     return len(div_list)
#
# num_div=12
# print(find_min_num(num_div))



