a=input()
if a.isdigit():
	z=0
	a=int(a)
	b=input().split()
	l=[]
	for i in range(0,a):
		if b[i].isdigit():
			l.append(b[i])
		else:
			z=z+1
	if z>0:
		print("Invalid")
	else:
		g=[]
		for j in range(1,len(l)):
			g.append(l[-j])
			g.append('->')
		g.append(l[0])
		print("".join(g))
else:
	print("Invalid")
