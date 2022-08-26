fc, fr = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
r_li = [0, fr]                      # 세로에 있는 지점을 표시하기 위한 리스트
c_li = [0, fc]                      # 가로에 있는 지점을 표시하기 위한 리스트
for i in range(N):
    if arr[i][0] == 0:              # 입력받은 값의 앞숫자가 0 일때는 세로이기 때문에 r 리스트에 추가
        r_li.append(arr[i][1])
    elif arr[i][0] == 1:            # 입력받은 값의 앞숫자가 1 일때는 가로이기 때문에 c 리스트에 추가
        c_li.append(arr[i][1])
r_li.sort(); c_li.sort()            # 오름차순으로 정렬

paper = []                          # 각 사각형의 꼭지점을 표시해주기 위한 리스트
for j in r_li:
    cut = []
    for i in c_li:
        cut += [(j, i)]
    paper.append(cut)
# [[(0, 0), (0, 4), (0, 10)], [(2, 0), (2, 4), (2, 10)], [(3, 0), (3, 4), (3, 10)], [(8, 0), (8, 4), (8, 10)]]

r_cnt, c_cnt = len(r_li), len(c_li)                 # 각 변의 꼭지점 개수
max_v = 0
for j in range(r_cnt-1):
    for i in range(c_cnt-1):
        y = paper[j+1][i+1][0] - paper[j][i][0]
        x = paper[j+1][i+1][1] - paper[j][i][1]
        value = y * x
        if max_v < value:
            max_v = value
print(max_v)