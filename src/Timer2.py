# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 16:17:59 2016

@author: LINONYMOUS
"""

import time
from CheckResult import check
#function that calls check() method after a specified amount of time i.e. period

def do_every(period,f):
    def g_tick(): #nested function
        t = time.time()
        count = 0
        while True:
            count += 1
            yield max(t + count*period - time.time(),0)
    g = g_tick()
    while True:
        time.sleep(next(g))
        f()

def hello():
    check() #call to check() method   
    time.sleep(.3)

do_every(60,hello) #time specified = 60 sec.