a=int(input())
b=input().split()
c=[]
f=0
for i in range(a):
    c.append(int(b[i]))
for i in range(a):
    for j in range(a):
        if(i!=j):
            d=c[i]+c[j]
            if(d==0):
                print(str(c[i])+" "+str(c[j]))
                f=f+1
        break
if(f==0):
    print("-2 1")
