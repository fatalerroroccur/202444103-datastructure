from collections import deque

d= deque([91,39,44])
d.append(-14)
d.appendleft(99)
d.append(99)
print(d.popleft())
print(d.popleft())
for _ in range(len(d)):
    print(d.popleft())