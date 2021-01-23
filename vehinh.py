#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
speed =0.05 #float(input('Speed: '))
import cv2
# Đọc file
a = list(open('pic.txt', 'r', encoding='UTF-8').read().split('\n'))

# hàm xóa màn hình console
def clear(): return os.system('cls')


x = max(map(lambda i: len(i), a))
clear()
k = 0
while k < x:
    for i in a:
        if(len(i) == 0):
            continue
        if(k > len(i)):
            print('\x1b[0;33;40m' + i[:len(i)] + '\x1b[0m')
            # for c in range(0,len(i)):
            #     print(i[c],end='')
        else:
            print('\x1b[0;33;40m' + i[:k+1] + '\x1b[1m')
            # for c in range(0, k+1):
            #     print(i[c],end='')

    time.sleep(speed)
    k += 1
    if(k != x):
        clear()
img = cv2.imread('img.png')
cv2.imshow("Happy birthday",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
