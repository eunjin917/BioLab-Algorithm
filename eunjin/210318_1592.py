# 영식이와 친구들
# https://www.acmicpc.net/problem/1592
# 2021.03.10

N, M, L = map(int, input().split())

countlist = [0 for i in range(N)] # 0으로 초기화한 길이N의 리스트
ball = 0 # 공의 위치
cnt = 0 # 공 몇 번 던지는지 횟수
countlist[ball] = 1 # 제일 첫사람이 공 받음

while(True):
    if countlist[ball] == M:
        break
        
    if (countlist[ball]%2) == 0: # 공 잡은 사람이 홀수 번째 잡았으면
        ball = ((ball+L)%N) # 시계방향으로 L번째 있는 사람에게 던짐
    else: # 공 잡은 사람이 짝수 번째 잡았으면
        ball = ((ball-L)%N) # 반시계방향으로 L번째 있는 사람에게 던짐
    countlist[ball] += 1 # 받은사람은 카운트
    cnt += 1 # 전체 횟수 카운트

print(cnt)