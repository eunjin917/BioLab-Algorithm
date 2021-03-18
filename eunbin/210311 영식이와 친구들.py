n, m, l = map(int, input().split())

people = {}
for i in range(1, n+1):
    people[i] = 0

count = 0
p = people[1] = 1
while people[p] != m:
    if people[p]%2 != 0:
        p = n
        
    else:
        p = (p-l)
        if p <= 0:
            p += n

    people[p] += 1
    count += 1

print(count)