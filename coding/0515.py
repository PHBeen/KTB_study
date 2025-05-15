from collections import deque
import sys

input = sys.stdin.readline

num_T = int(input())
arr_parentheses = [input().strip() for _ in range(num_T)]


for line in arr_parentheses:
    queue = deque()
    for word in line:
        if word == "(":
            queue.append("(")
        else:
            if len(queue) == 0:
                queue.append(")")
                break
            else:
                queue.pop()
                 

    if len(queue) == 0:
        print("YES")
    else:
        print("NO")

        