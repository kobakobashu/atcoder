n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

for i in range(1, len(num_list) + 1):
    if i != num_list[i - 1]:
        print("No")
        exit()

print("Yes")

"""
time : 2m
time complexity : O(nlogn)
space complexity : O(1)
"""