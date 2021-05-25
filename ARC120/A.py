N = int(input())
A_list = list(map(int, input().split()))

output_list = []
sum_to_i = A_list[0]
max = A_list[0]
max_last_list = 2 * A_list[0]
output_list.append(max_last_list)
for i in range(1, len(A_list)):
    sum_to_i += A_list[i]
    if max < A_list[i]:
        diff = (A_list[i] - max) * i + sum_to_i + A_list[i]
        output_list.append(output_list[i - 1] + diff)
        max = A_list[i]
        max_last_list = sum_to_i + A_list[i]
    else:
        output_list.append(output_list[i - 1] + A_list[i] + max_last_list)
        max_last_list = A_list[i] + max_last_list

for num in output_list:
    print(num)

"""
time : 15m
time complexity : O(N)
space complexity : O(N)
"""