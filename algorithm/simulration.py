n, m =map(int, input().split())
# n == row / m == column

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

x,y,direction = map(int,input().split())
d[x][y] = 1 # 현재 위치하고 있는 좌표를 방문한 것으로 표시하기

array  = [] # 전체적인 맵을 표시하기 위한 리스트
for i in range(n):
    array.append(list(map(int,input().split()))) # row 만큼 반복하기 0 : 육지 1 : 바다


# 북 동 남 서 방향 정의하기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]


# 왼쪽으로 회전하기

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # turn left
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우에 이동시키기
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우에 처리하는 구문
    else:
        turn_time += 1

    # 4 방향 전부다 갈 수 없을 때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)