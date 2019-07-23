#r
ln=list(map(int,input().split()))
r=ln[0]
s=ln[1]
r=r^s
s=r^s
r=r^s
print(r,s)
