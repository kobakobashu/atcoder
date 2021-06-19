"""
尺取り法
"""
n, q = map(int, input().split())
a_list = list(map(int, input().split()))
num_list = [int(input()) for _ in range(q)]

new_num_list = []
for idx, num in enumerate(num_list):
    new_num_list.append([num_list[idx], idx])

sorted_num_list = sorted(new_num_list, key=lambda x: x[0])

j = 0

for i in range(q):
    if j < n:
        while  a_list[j] <= sorted_num_list[i][0] + j:
            j += 1
            if j == n:
                break
    sorted_num_list[i][0] = sorted_num_list[i][0] + j

output = sorted(sorted_num_list, key=lambda x: x[1])

for i in range(len(output)):
    print(output[i][0])

"""
time : 20m
time complexity : O(n + q + qlogq)
space complexity : O(q)
"""