#숫자 변환하기
from collections import deque


def solution(x, y, n):
    def bfs(x, y, n):
        q = deque()
        dist[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if x + n <= y and dist[x + n] == 0:
                dist[x + n] = dist[x] + 1
                q.append(x + n)
            if x * 2 <= y and dist[x * 2] == 0:
                dist[x * 2] = dist[x] + 1
                q.append(x * 2)
            if x * 3 <= y and dist[x * 3] == 0:
                dist[x * 3] = dist[x] + 1
                q.append(x * 3)

    dist = [0] * (y+1)
    bfs(x,y,n)

    return dist[y]-1