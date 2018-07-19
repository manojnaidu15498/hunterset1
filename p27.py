n=input()
k=[]
for i in range(0,len(n)):
	k.append(n[i])
d="".join(k[::-1])
if n!=d:
	print(n)
elif n==d:
	z=[]
	for i in range(0,len(n)-1):
		z.append(k[i])
	print("".join(z))
