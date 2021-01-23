# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import time
# t=float(input("time: "))
# import os
# clear = lambda: os.system('cls') #on Windows System

# print(" ███▄    █ ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄            ███▄ ▄███▓▓█████ ")
# time.sleep(t)
# print(" ██ ▀█   █ ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄         ▓██▒▀█▀ ██▒▓█   ▀ ")
# time.sleep(t)
# print("▓██  ▀█ ██▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄       ▓██    ▓██░▒███   ")
# time.sleep(t)
# print("▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██      ▒██    ▒██ ▒▓█  ▄ ")
# time.sleep(t)
# print("▒██░   ▓██░░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒ ██▓ ▒██▒   ░██▒░▒████▒")
# time.sleep(t)
# print("░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░ ▒▓▒ ░ ▒░   ░  ░░░ ▒░ ░")
# time.sleep(t)
# print("░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░ ░▒  ░  ░      ░ ░ ░  ░")
# time.sleep(t)
# print("   ░   ░ ░  ░ ░  ░   ░   ▒    ░        ░   ▒    ░   ░      ░      ░   ")
# time.sleep(t)
# print("         ░    ░          ░  ░              ░  ░  ░         ░      ░  ░")
# time.sleep(t)
# print("            ░                                    ░                    ")
# time.sleep(t)
# clear()
x=[1,2,3,4,5,6,7,8,9]
a=map(lambda i:i+i,x)
print(list(a))
import time
import os
clear = lambda: os.system('cls') #on Windows System
for i in range(1,100):
    for j in range(1,10):
        print(i*'*')
    time.sleep(0.5)
    clear()
    
