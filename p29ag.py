a=int(input())
b=input().split()
c=len(b)
m=0
d=[]
n=0
for i in range(c):
        d.append(int(b[i]))
for i in d:
        if(i>0):
                m=m+i
                n=n+1
if(n==0):
    d.sort()
    print(d[c-1])
else:
    print(m)
