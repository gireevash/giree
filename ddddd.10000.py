from itertools import combinations
o,i=map(int,input().split())
u=len(str(o))
r=list(combinations(str(o),u-i))
r=sorted(r)
print("".join(r[0]))
