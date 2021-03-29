// https://www.acmicpc.net/problem/2292

N=int(input("N값: "))
count=1; 
room=1; #거치는 방의 수

value=int(N/6) 
#6각형이 군집된 형태라 일차적으로 6으로 나눔

if(N==1):
    print("1")
    exit()
    

while(value>count):
    room+=1; #방을 하나씩 더 거침
    count=count+room #방을 거칠때 증가하는 피보나치
    

if(N==count*6+1):
    room-=1;

print("\n 거쳐야 하는 방의 개수: ", room+1, "\n")
