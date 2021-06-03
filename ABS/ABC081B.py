n = int(input())
num_list = list(map(int, input().split()))

max_div_num = 0
while True:
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            num_list[i] = num_list[i] // 2
        else:
            print(max_div_num)
            exit()
    max_div_num += 1

"""
time : 3m
time complexity : O(n^2)
space complexity : O(1)
"""