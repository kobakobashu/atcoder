n = int(input())
num_list = list(map(int, input().split()))

output = 0
for num in num_list:
    if num > 10:
        output += (num - 10)
print(output)

"""
time : 2m
time complexity : O(len(nums_list))
space complexity : O(1)
"""