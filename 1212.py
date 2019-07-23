#f
f=list(input())
g=" "
for v in range(len(f)):
    if g in f:
        f.remove(g)
print(len(f))
