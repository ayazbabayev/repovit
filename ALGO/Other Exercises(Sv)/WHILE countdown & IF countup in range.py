# COUNTDOWN: WHEN "3", PRINT "THREE".

def countdown_1(x):
    while x >= 0:   #(or) while x!=0:

        if x == 3:
            print("three")
        else:
            print(x)

        x -= 1

countdown_1(5)


# def countdown_2(x):
#     while x >= 0:
#         print(x)
#         x -= 1
#
#         if x == 3:
#             print('three')
#             x-=1
#
# countdown_2(4)

print('#############################################################################################################\n')

def countdownrange(x):
    for n in range(x,-1,-1):
        if n==4:
            print('DORT')
        else:
            print(n)

countdownrange(5)


def countup(x):
    for no in range(0,x+1):
        if no == 5:
            print('five')
        else:
            print(no)

countup(10)

########################################################################################################################

