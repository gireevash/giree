sun,mun=map(int,input().split())
for u in range(sun+1,mun):
    for v in range(2,u):
         if(u%v==0):
           break
    else:
      print(u,end=" ")
