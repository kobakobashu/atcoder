num_list = list(map(int, input().split()))

from math import comb

A = num_list[0]
B = num_list[1]
K = num_list[2]

output_list = []
while A or B:
    comb_start_a = comb(A + B - 1, B)
    if  K <= comb_start_a:
        output_list.append("a")
        A = A - 1
    else:
        output_list.append("b")
        B = B - 1
        K = K - comb_start_a
print(''.join(output_list))

"""
time : 30m
time complexity : O(A + B)
space complexity : O(A + B)
"""