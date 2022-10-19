N = int(input())
arr = list(map(int, input().split()))
visited = [1 for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            visited[i] = max(visited[i], visited[j] + 1)
print(max(visited))
