import sys; sys.stdin = open('input/5356_input.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [[] for _ in range(5)]
    for i in range(5):
        arr[i] += list(map(str, input()))

    print(arr)
    # max_l = long_s = 0
    # for i in st:
    #     long_s = len(i)
    #     if max_l < long_s:
    #         max_l = long_s
    # for i in range(max_l):
    #     for j in range(5):
    #         print(st[j][i], end='')
    # print()