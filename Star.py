# -*- coding: utf-8 -*-
"""

@author: Srinu-sai
"""
import turtle
wn = turtle.Screen() 
x = turtle.Turtle()

n = int(input('Number of points(odd & >=5):'))
if n%2 == 0:
    print('Please enter an odd number greater than or equal to 5!')
elif n<5:
    print('Please enter an odd number greater than or equal to 5!')
else:
    x.left(360/n)
    
    for i in range(n):
        x.forward(200)
        x.right(180-180/n)
    print('Here is your '+str(n)+' pointed star :)')
