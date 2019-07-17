arr1=int(input())
arr2=[]
arr3=[]
for i in range(arr1):
  arr3=input()
  arr2.append(arr3)
hit=[]
for i in zip(*arr2):
  if(i.count(i[0])==len(i)):
    hit.append(i[0])
  else:
    break
print(''.join(hit))
