def DFS_Explore(u, time, time_1, time_2, visited, p):
    time += 1
    time_1[u] = time
    visited[u] = True

    for v in range(len(visited)):
        if not visited[v]:
            p[v] = u
            time = DFS_Explore(v, time, time_1, time_2, visited, p)

    time += 1
    time_2[u] = time
    return time

def DFS(g):
    n = len(g)
    visited = [False] * n
    p = [-1] * n
    time = 0
    time_1 = [0] * n
    time_2 = [0] * n

    for u in range(n):
        if not visited[u]:
            time = DFS_Explore(u, time, time_1, time_2, visited, p)

    return p, time_1, time_2


g = [
    [1, 2],
    [0, 3, 4],
    [0, 5],
    [1],
    [1, 6],
    [2],
    [4, 7],
    [6]
]

poprzednik, time_1, time_2 = DFS(g)

for x in range(len(poprzednik)):
    print(f"Wierzchołek {x}: poprzednik - {poprzednik[x]}, time_1 - {time_1[x]}, time_2 - {time_2[x]}")
