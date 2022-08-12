T = int(input())
cow_dict = {}
cnt = 0
for test_case in range(1, T+1):
    c, m = map(int, input().split())
    if c in cow_dict:
        if cow_dict[c] != m:
            cnt += 1
            cow_dict[c] = m
    else:
        cow_dict[c] = m
print(cnt)