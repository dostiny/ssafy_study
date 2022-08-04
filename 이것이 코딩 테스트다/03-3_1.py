n, m = map(int, input().split())

minnum_list = []
for i in range(n):
    li = sorted(list(map(int, input().split())))
    minnum_list.append(li[0])
    minnum_list.sort(reverse=True)

print(minnum_list[0])