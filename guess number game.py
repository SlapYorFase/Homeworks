# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 18:29:11 2022

@author: Philip
"""
lol=0
import random
num=random.randint(1,100)
while (lol!=num):
    lol=int(input("\nYour number is:"))
    if num>lol:
        print ("\ntoo low bro(higher)")
    elif num<lol:
        print("\n too High sucka(lower)")
    else:
        print("Congratulations team, we've played this well.(it means that you got it right)")
      
        