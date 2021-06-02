num_list = list(map(int, input().split()))

output_1 = 0
output_100 = 0

for i in range(1, num_list[1] + 1):
    output_1 += i
output_1 = output_1 * num_list[0]

for i in range(1, num_list[0] + 1):
    output_100 += i * 100
output_100 = output_100 * num_list[1]
output = output_1 + output_100

print(output)

"""
time : 7m
time complexity : O(m)    m : max(N, K)
space complexity : O(1)
"""