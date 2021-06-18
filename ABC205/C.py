A, B, C = map(int, input().split())

if C % 2 == 0:
    A = abs(A)
    B = abs(B)
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")

else:
    if 0 <= A and 0 <= B:
        if A < B:
            print("<")
        elif A > B:
            print(">")
        else:
            print("=")

    if A < 0 and B < 0:
        if A < B:
            print("<")
        elif A > B:
            print(">")
        else:
            print("=")

    elif A < 0:
        print("<")
    elif B < 0:
        print(">")

"""
time : 5m
time complexity : O(1)
space complexity : O(1)
"""