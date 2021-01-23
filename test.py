a=input().split(' ')
b=input().split(' ')
c=[]
for i in a:
    if i =='':
        continue
    if i not in b:
        c.append(i)
c.sort()
c=set(c)

print(' '.join(c))

    
    
