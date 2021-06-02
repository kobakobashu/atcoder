num_list = list(map(int, input().split()))
num_list.sort()
if num_list[0] == num_list[1]:
    print(num_list[2])
elif num_list[1] == num_list[2]:
    print(num_list[0])
else:
    print(0)

"""
time : 2m
time complexity : O(1)
space complexity : O(1)
"""