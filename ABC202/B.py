S = input()

S_list = list(S)
S_list.reverse()
for i in range(len(S_list)):
    if S_list[i] == "6":
        S_list[i] = "9"
    elif S_list[i] == "9":
        S_list[i] = "6"
print(''.join(S_list))

"""
time : 5m
time complexity : O(len(S))
space complexity : O(len(S))
"""