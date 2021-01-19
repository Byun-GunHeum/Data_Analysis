a= set(range(1,10001))
b=set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    b.add(i)
c=a-b
for k in sorted(c):
    print(k)