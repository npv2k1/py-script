import os
import shutil
#Loc cac tep
list=os.listdir()
Compressed=('zip','rar','7z')
Documents=('xlsx','doc','pdf','txt','pptx')
Picture=('jpg','PNG')
Programs=('exe','msi')
Video=('mp4')
Music=('mp3','flac')
#cac folder
listdir=('Picture','Documents','Programs','Video','Music','Compressed')

for i in listdir:
    if(os.path.exists(os.path.join(os.getcwd(), i))):
        pass
    else:
        os.mkdir(os.path.join(os.getcwd(), i))
#loc file
for i in list:
    if (os.path.isfile(os.path.join(os.getcwd(), i))):
        a=i.split('.')
        if(a[len(a)-1] in Picture):
            try:
                shutil.move(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), 'Picture',i))
            finally:
                pass
        if (a[len(a) - 1] in Documents):
            try:
                shutil.move(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), 'Documents', i))
            finally:
                pass
        if (a[len(a) - 1] in Programs):
            try:
                shutil.move(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), 'Programs', i))
            finally:
                pass
        if (a[len(a) - 1] in Video):
            try:
                shutil.move(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), 'Video', i))
            finally:
                pass
        if (a[len(a) - 1] in Compressed):
            try:
                shutil.move(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), 'Compressed', i))
            finally:
                pass
        if (a[len(a) - 1] in Music):
            try:
                shutil.move(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), 'music', i))
            finally:
                pass


#print(os.path.isfile(os.path.join(os.getcwd(),'a.jpg')))
#shutil.move(os.path.join(os.getcwd(),'a.jpg'),os.path.join(os.getcwd
