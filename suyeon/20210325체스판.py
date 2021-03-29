import copy

b_count=0
w_count=0
min_count=0

while True :# n, m 입력 받음 (8이상 50이하가 아니면 재입력)
    n, m = map(int, input().split())
    if (8<=n<=50 and 8<=n<=50) :
        break
    print("재입력\n")

chess=[] #빈 리스트 생성

for i in range(n) : #체스판 상태 입력
    chess.append(list(input())) 
    
i=0

temp=[[0 for i in range (8)] for j in range (8)] #복사할 임의 체스판(white랑 black만들기 위해서)
white_chess=copy.deepcopy(temp) #'W'가 좌측상단인 체스판
black_chess=copy.deepcopy(temp) #'B'가 좌측상단인 체스판

i,j=0,0

for i in range(8): #최상단 왼쪽이 W인 이차원 배열
    for j in range(8):
        
        if i%2==0:#행 인덱스가 짝수일때는 W먼저 시작
            if j%2==0:
                white_chess[i][j]='W'
            else:
                white_chess[i][j]='B'


        else: #행 인덱스가 홀수일때는 B먼저 시작
            if j%2==0:
                white_chess[i][j]='B'
            else:
                white_chess[i][j]='W'

i,j=0,0
for i in range(8): #최상단 왼쪽이 B인 이차원 배열 
    for j in range(8):

        if i%2==0: #행 인덱스가 짝수일때는 B먼저 시작
            if j%2==0:
                black_chess[i][j]='B'
            else:
                black_chess[i][j]='W'


        else: #행 인덱스가 홀수일 때는 W먼저 시작
            if j%2==0:
                black_chess[i][j]='W'
            else:
                black_chess[i][j]='B'

i,j=0,0
min_count=32 #8*8체스판에서 최대로 안 맞을 수 있는 크기

while(i<=n-8): #행인덱스
    j=0
    while(j<=m-8): #열인덱스
        newchess=copy.deepcopy([row[j:j+8]for row in chess [i:i+8]]) #8*8의 부분 행렬
        for x in range(8): #부분행렬 검사 반복문
            for y in range(8): #두 종류의 체스판 중 어느 쪽이 효율적인지 비교
                if newchess[x][y]!=white_chess[x][y]: 
                    w_count+=1
                if newchess[x][y]!=black_chess[x][y]:
                    b_count+=1
        if(min_count>min(w_count,b_count)):
           min_count=min(w_count, b_count)

        w_count=0
        b_count=0
        x=0
        y=0
        print("\n")

        j+=1
    i+=1 
        
print(min_count)
