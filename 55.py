m=int(input())
n=m
p=0
while y!=0:
  d=y%10
  p=p*10+d
  m=m//10
if(p==n):
  print('yes')
else:
print('no')
