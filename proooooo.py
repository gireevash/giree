pqr,xyz=input().split()
cost_diff1=abs(len(pqr)-len(xyz))
for l in range(len(pqr)):
    if len(xyz)==1 and xyz[l] in pqr:
        break
    if pqr[l] != xyz[l]:
        cost_diff1+=1 
print(cost_diff1)
