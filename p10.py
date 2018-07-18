n,m=input().split()
n=int(n)
m=int(m)
a=input().split()
b=input().split()
q=0
e=[]
f=[]
for i in range(n):
    e.append(a[i])
for i in range(m):    
    f.append(b[i])
for i in e:
    for j in f:
        if(i==j):
            q=q+1
if(q==m):
    print("YES")
else:
    print("NO")
