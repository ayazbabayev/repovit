# REVERSE INTEGER:
# 123 to 321.

def reverse_int(n):
    string = str(n)

    if string[0] == '-':              # If 1st ele in string = minus (negative)
        return int('-'+string[:0:-1])  # Convert it to int, start from last ele, STOP AT 1st "0" ele
    else:                              # If not negative
        return int(string[::-1])       # return it in reverse

test1 = 123
test2 = -456
test1_result= reverse_int(test1)
test2_result= reverse_int(test2)
print(test1_result)
print(test2_result)


#EXTRA SOURCE:
string = "America"
print(string[::])              # America (straight)
print(string[::-1])            # aciremA (reverse)
print(string[len(string)//2])     # r       (MIDDLE)
print(string[1::])             # merica  (from 2nd value)
print(string[:2])             # Am      (1st 2 letters)
print(string[1::-1])           # mA      (1st 2 letters but reverse)

test_list = [1,2,3,4,5,6]
print(test_list[::3])       # jumps to every 2nd number
# test_list[starting_index:end index: step]


#############################################################################################################################################

