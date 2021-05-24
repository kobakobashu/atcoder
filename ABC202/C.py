from collections import Counter

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

output = 0
B_C_list = []
for i in range(N):
    B_C_list.append(B_list[C_list[i] - 1])

B_C_list_counter = Counter(B_C_list)
for num in A_list:
    output += B_C_list_counter[num]

print(output)

"""
time : 10m
time complexity : O(N)
space complexity : O(N)
"""