# INSERTION:
# DEF:
# like card game. 1st selected card is sorted. we select an unsorted card.
# If unsorted is > card in hand, we place it on right, otherwise, left.
# Other cards are taken and put at their right place too.

# Similar approach is used by insertion.
# insertion sort algo places an unsorted ele at its suitable place in ea iteration.
# list = [1,5,3,4,6,8,6,2]
# List used in example below = [2,1,4]

def insertion_sort(list):
    for i in range(1, len(list)):                   # first card - index 0 - was sorted: "2". So we begin with 2nd card -index 1- which is "1".
        key = list[i]                               # key = "1".             any element in list ? all elements in list?
        p = i - 1                                   # "2"

        while p >= 0 and key < list[p]:             # while 2 >= 0 and 1 < 2's index (value 2)
            list[p + 1] = list[p]                   # 2 = 1's place
            p -= 1                           # Q: ??? HOW PREV EQUALS TO -1??? 1:29:56 WHAT IS -1...REMOVAL?
                                             # BECAUSE -1 AND >=0 RULE HE GETS OUT OF LOOP. WAS 0 INDEX? OR VALUE?
        list[p + 1] = key                    # PREV # HOW TO KNOW IF indentation is True or False WITHOUT else?

    return list

list_sort = [2, 1, 4]
print('original list:',list_sort)
result=insertion_sort(list_sort)
print(result)
