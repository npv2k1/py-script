from random import randint
from asciimatics.screen import Screen
import time

a = list(open('pic.txt', 'r', encoding='UTF-8').read().split('\n'))

x = max(map(lambda i: len(i), a))

def demo(screen):
    hei=0
    k = 0
    while k < x:
        hei=0
        for i in a:
            if(len(i) == 0):
                continue
            if(k > len(i)):                
                screen.print_at(i[:len(i)], 0, 1*hei)
                screen.refresh()
                hei+=1
            else:
                screen.print_at(i[:k+1],0,1*hei)
                hei+=1
                screen.refresh()
            ev = screen.get_key()
            if ev in (ord('Q'), ord('q')):
                return
        screen.refresh()
        time.sleep(0.05)
        k+=1
        if(k != x):       
            screen.clear()


Screen.wrapper(demo)
