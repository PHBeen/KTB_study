from collections import deque
import sys

input = sys.stdin.readline  # 입력도 빠르게
num = int(input())
orders = [input().split() for _ in range(num)]

queue = deque()
for order in orders:
    command = order[0]
    if command == "push":
        queue.append(order[1])

    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif command == "size":
        print(len(queue))
        
    elif command == "empty":
        print(0 if queue else 1)
    
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
