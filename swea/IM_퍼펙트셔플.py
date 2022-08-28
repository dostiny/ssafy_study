import sys; sys.stdin = open('input/IM_셔플_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    card = list(map(str, input().split()))
    n = len(card)
    if n%2 == 0:
        fn = n // 2
        sn = n - fn
    else:   # 홀수
        fn = n // 2 + 1
        sn = n - fn
    fcard, scard = [], []
    for i in range(fn):
        fcard.append(card[i])
    for j in range(fn, n):
        scard.append(card[j])

    result = []
    for k in range(sn):
        result += [fcard[k], scard[k]]
    if fn - sn == 1:
        result += [card[fn-1]]
    print(f'#{tc}', *result)