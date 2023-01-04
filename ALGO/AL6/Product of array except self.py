# Given an integer array nums return an array answer such that
# answer[i] (element @ index i) equals to the product of all elements of nums except nums[i] (nums at index i)
# example:

# input: nums = [1,2,3,4]
# output: [24,12,8,6] yani multiply all eles except self
# except 1: (2*3*4)
# except 2: (1*3*4)
# except 3: (1*2*4)
# except 44: (1*2*3)

def product_of_array(arr):
    result = [1] * len(arr)                         # Q: Meaning?
    print('result:',result)                         # Q: how this turns [1,1,1,1] ?
    print('len(arr):',len(arr))                     # 4

    for i in range(len(arr)):
        for x in range(len(arr)):
            if i != x:
                result[i] = result[i] * arr[x]      # result@index i = result@index i * arr@index x
                print(result[i])                    # Q: Meaning? and how result above is related to result[i]
    return result

test_list = [1,2,3,4]
result = product_of_array(test_list)
print(result)