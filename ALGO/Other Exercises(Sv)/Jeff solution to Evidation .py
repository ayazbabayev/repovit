def solution(S):
    # if S == "011100":
    #     V = 28
    # if S == "111":
    #     V = 5
    # if S == "111101010111":
    #     V = 22
    V = int(S, 2) # --> 0,1
    no = 0

    while V > 0:
        if V % 2 == 0:
            V = V / 2
        else:
            V = V - 1
        no = no + 1

    return no

S= '101010101010101010101'
result = solution(S)
print(result)