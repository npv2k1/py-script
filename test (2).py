import  time
t=time.time()
f=open('1-10.txt','r',encoding='UTF-8')

b=f.read().split(',')
print(set(b))
print('time: ', time.time()-t)
