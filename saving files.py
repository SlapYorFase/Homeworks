# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:39:49 2022

@author: Philip
"""
import time
sss=int(input("Number of files:"))
lol=[]
if sss==0:
    print("get out.")
    time.sleep(1.5)
    print("\nGET OUT like here man!")
else: 
    for i in range(sss):
        hot=(input("File name:"))
        lol.append(hot)
        print("\nYour files saved now:",*lol)
    time.sleep(2)
    print("\nYou finally done?")
    time.sleep(2)
    print("\nAll files saved:", *lol)



