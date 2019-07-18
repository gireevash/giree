giree=int(input())
giree=list(map(int,input().split()))
madhu=[]
for s in giree:
	if(giree.count(s)>=2 and s not in madhu):
		madhu.append(k)
if(len(madhu)==0):
	print("unique")
else:
	for s in madhu:
		print(s,end="")
