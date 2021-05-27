num_list = list(map(int, input().split()))
str_list = [input() for _ in range(num_list[0])]

color_list = [0] * (num_list[0] + num_list[1] - 1)
for i in range(num_list[0]):
    for j in range(num_list[1]):
        if str_list[i][j] == "B":
            if color_list[i + j] == "R":
                print(0)
                exit()
            else:
                color_list[i + j] = "B"
        elif str_list[i][j] == "R":
            if color_list[i + j] == "B":
                print(0)
                exit()
            else:
                color_list[i + j] = "R"
output = 2 ** color_list.count(0)
output = output % 998244353
print(output)
"""
time : 40m
time complexity : O(HW)
space complexity : O(HW)
"""