# REVERSE STRING: # abcde -> edcba

# SOLUTION 1:
def reverse_string(s):
    return s[::-1]

test_str = "hello"
test_result = reverse_string(test_str)
print(test_result)  #olleh


# SOLUTION 2:
# ALTERNATIVE IS INSERT!

def str_reverser(x):
    # return x[::-1]
    list = []
    for i in x:
        list.insert(0, i)
        joined = ''.join(list)
    return joined

test = 'alaku'
result = str_reverser(test)
print(result)

################################

def reves(x):
    list= []
    for v in x:
        list.insert(0,v)
        join = ''.join(list)
    return join

print(reves(x='tinder'))
########################################################################################################################
