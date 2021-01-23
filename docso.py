dictSo={
    1:'một',
    2:'hai',
    3:'ba',
    4:'bốn',
    5:'năm',
    6:'sáu',
    7:'bảy',
    8:'tám',
    9:'chín',
}
#x=input("nhap 1 số: ")

def outputs(tram,chuc,donvi):
    if(tram==0):
        if(chuc!=0 and donvi !=0):
            return dictSo[chuc] + ' mươi ' +dictSo[donvi]
        elif(chuc==0):
            return dictSo[donvi]
        else:
            dictSo[chuc] + ' mươi '
    else:
        return dictSo[tram]+' trăm '+dictSo[chuc] + ' mươi ' + dictSo[donvi]

a=outputs(1,1,1)
print(a)
