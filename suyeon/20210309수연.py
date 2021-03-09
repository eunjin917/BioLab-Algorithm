N=int(input("N값: "))
count=1;
room=1;

value=int(N/6)

if(N==1):
    print("1")
    exit()
    

while(value>count):
    room+=1;
    count=count+room
    

if(N==count*6+1):
    room-=1;

print("\n 거쳐야 하는 방의 개수: ", room+1, "\n")
