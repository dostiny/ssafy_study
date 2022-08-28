# import sys; sys.stdin = open('input/IM_메모리복구_input.txt', 'r')

for tc in range(1, int(input())+1):
    memory = list(map(int, input()))
    n = len(memory)
    init_v = [0] * n
    cnt = 0
    idx = 0
    while idx != n:
        if init_v[idx] != memory[idx]:
            if memory[idx] == 1:
                cnt += 1
                for i in range(idx, n):
                    init_v[i] = 1
            else: # memory[idx] == 0:
                cnt += 1
                for i in range(idx, n):
                    init_v[i] = 0
        idx += 1
    print(f'#{tc} {cnt}')
