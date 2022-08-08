n = int(input())
t_set = set()
t_table = []

for i in range(n):
    t = list(map(int, input().split())) 
    start_t = t[0]
    end_t = t[-1]+1

    for j in range(start_t, end_t):
        t_set.add(j)
    
    t_table.append(t_set)
    t_set = set()

t_count = 1
max_count = 0

for x in t_table:
    full_t = x
    for y in t_table:
        if len(full_t & y) == 0:
            full_t = full_t | y
            t_count += 1
    if max_count <= t_count:
        max_count = t_count
    t_count = 1

print(max_count)