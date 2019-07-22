gk,rk=map(int,input().split())
for v in range(gk,rk):
  tm=0
  temp=v
  while(temp>0):
     tm=tm+(temp%10)**3
     temp=temp//10
  if(tm==v):
     print(v,end=" ")
