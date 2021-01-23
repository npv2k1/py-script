import time
a=[2,3,7,8,9,0,2,3,4,1,8,7,3,4,6,9,8,5,2,4,1,3,9,8]
i=len(a)-1
dem=0

t=time.time()
for j in range(0,len(a)):
    for k in range(1,len(a)-j):
        if(a[i]<a[i-1]):
            a[i],a[i-1]=a[i-1],a[i]
        i-=1
    i=len(a)-1
print(a)
print('done in: ',time.time()-t)
a=[2,3,7,8,9,0,2,3,4,1,8,7,3,4,6,9,8,5,2,4,1,3,9,8]
t=time.time()
a.sort()
print(a)
print('done in: ',time.time()-t)


