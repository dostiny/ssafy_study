t = int(input())

count = 0
for h in range(t+1):    # 시간
    for m in range(60): # 분
        for s in range(60): # 초
            arr = [int(b) for b in str(h)] + [int(b) for b in str(m)] + [int(b) for b in str(s)]
            if 3 in arr:
                count += 1

print(count)