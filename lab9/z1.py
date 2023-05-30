from collections import deque


def bfs(g, s):
    n = len(g)
    visited = [False] * n
    distance = [-1] * n
    parent = [-1] * n

    visited[s] = True
    distance[s] = 0
    q = deque()
    q.append(s)

    while q:
        u = q.popleft()
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                q.append(v)

    return distance, parent
