#b
p=input()
q=0
for v in range(len(p)):
    if (p[v].isalpha() or p[v].isnumeric() or p[v]==" "):
      continue
    q=q+1
else:
    print(q)
