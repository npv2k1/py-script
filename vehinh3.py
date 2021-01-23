#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
# string1 = """
#  ██▓    ██▓     ▒█████   ██▒   █▓▓█████    ▓██   ██▓ ▒█████   █    ██ 
# ▓██▒   ▓██▒    ▒██▒  ██▒▓██░   █▒▓█   ▀     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒
# ▒██▒   ▒██░    ▒██░  ██▒ ▓██  █▒░▒███        ▒██ ██░▒██░  ██▒▓██  ▒██░
# ░██░   ▒██░    ▒██   ██░  ▒██ █░░▒▓█  ▄      ░ ▐██▓░▒██   ██░▓▓█  ░██░
# ░██░   ░██████▒░ ████▓▒░   ▒▀█░  ░▒████▒     ░ ██▒▓░░ ████▓▒░▒▒█████▓ 
# ░▓     ░ ▒░▓  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░      ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ 
#  ▒ ░   ░ ░ ▒  ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ 
#  ▒ ░     ░ ░   ░ ░ ░ ▒       ░░     ░       ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░ 
#  ░         ░  ░    ░ ░        ░     ░  ░    ░ ░         ░ ░     ░     
#                              ░              ░ ░                       
# """
f=open('pic.txt','r',encoding='UTF-8')
string1=f.read()
a = list(string1.split('\n'))
# print(a)


def clear(): return os.system('cls')  # on Windows System


clear()
k = 0
while k<len(a[1]):
    for i in a:
        if(len(i)==0): 
            break;
        #for j in range(0,k):
            #print(i[j],end='')
        # print('\x1b[0;31;40m' + i[:k+1] + '\x1b[0m')
        print(i[:k+1])
        
        
    time.sleep(0.05)
        #clear()
    k += 1
    if(k!=len(a[1])):
        clear()
    
# print(string1)


# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
#     for style in range(8):
#         for fg in range(30, 38):
#             s1 = ''
#             for bg in range(40, 48):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#             print(s1)
#         print('\n')


# print_format_table()
