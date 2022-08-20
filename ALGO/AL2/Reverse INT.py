# REVERSE INTEGER:
# 123 to 321.

def reverse_int(n):
    string = str(n)

    if string[0]  == '-':              # If 1st ele in string = minus (negative)
        return int('-'+string[:0:-1])  # Convert it to int and start from last ele
    else:                              # If not negative
        return int(string[::-1])       # return it in reverse

test1 = 123
test2 = -456
test1_result= reverse_int(test1)
test2_result= reverse_int(test2)
print(test1_result)
print(test2_result)


#EXTRA SOURCE:
str = "America"
print(str[::])              # America (straight)
print(str[::-1])            # aciremA (reverse)
print(str[len(str)//2])     # r       (MIDDLE)
print(str[1::])             # merica  (from 2nd value)
print(str[:2])             # Am      (1st 2 letters)
print(str[1::-1])           # mA      (1st 2 letters but reverse)

test_list = [1,2,3,4,5,6]
print(test_list[::3])       # jumps to every 2nd number
# test_list[starting_index:end index: step]

