# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 07:39:12 2022

@author: Philip
"""
total=0
bag=[]
SHOP= {"banana":25,
        "apple":35,
        "milk":105, 
        "cake":85,
        "egg":10}
num=int(input("quantity:"))
if num==0:
    print("get out of here")
else:
    for i in range(num):
        userin=input("enter:")
        bag.append(userin)
        total+=SHOP[userin]
    print("\nbag--->",*bag)
    print("\ntotal--->",total)