h = int(input())

count = 0
for t in range(h+1):
    for m in range(60):
        for s in range(60):
            arr = [int(b) for b in str(t)] + [int(b) for b in str(m)] + [int(b) for b in str(s)]
            if 3 in arr:
                count += 1

print(count)