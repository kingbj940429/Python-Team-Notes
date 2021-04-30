from collections import deque

data = deque([2, 3, 4])
data.append(5)
data.appendleft(1)

print(data)
print(list(data))

data.pop()
data.popleft()

print(data)
print(list(data))

