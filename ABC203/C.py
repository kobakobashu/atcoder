N, K = list(map(int, input().split()))
friend_list = [list(map(int, input().split())) for _ in range(N)]
friend_list_sort = sorted(friend_list, key=lambda x: x[0])
for i in range(N):
    if K < friend_list_sort[i][0]:
        print(K)
        exit()
    else:
        K = K + friend_list_sort[i][1]
print(K)

"""
time : 10m
time complexity : O(N)
space complexity : O(N)
"""