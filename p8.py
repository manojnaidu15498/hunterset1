a=int(input())
b=input().split()
z=[]
for i in range(a):
    z.append(int(b[i]))
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            d=z[i]+z[j]
            if(d==z[k]):
                print(str(z[i])+" "+str(z[j])+" "+str(z[k]))
