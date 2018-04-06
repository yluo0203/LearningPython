#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:31:30 2018

@author: tse-jen.lu
"""

#import matplotlib.pyplot as mpt

#Ref:Numpy Tutorials | 1. Lists vs Arrays: https://youtu.be/WmXiPyEcChg
import numpy as np
L = [1, 2, 3]
A = np.array([1, 2, 3])
print("This is a python list:", L)  #This is a python list: [1, 2, 3]
print ("This is a np.array:", A)    #This is a np.array: [1 2 3]
print ("This is 2 * L: ", 2 * L)    #This is 2 * L:  [1, 2, 3, 1, 2, 3]
print ("This is 2 * A: ",2 * A)     #This is 2 * A:  [2 4 6]

print ()
#Ref: Numpy Tutorials | 2. Dot product 1 For loop vs cosine method vs dot function: https://youtu.be/GSxLKQNoXqM
a = np.array([1, 2])
b = np.array([2, 1])

dot = 0
for e, f in zip(a, b):
    dot += e * f
    
print ("dot is:",dot)                                   #dot is: 4
print ("or, I can say np.dot(a, b) is:", np.dot(a, b))
print ("a * b is:", a * b)                              #a * b is: [2 2]
print ("np.sum(a*b) is :", np.sum(a * b))               #np.sum(a*b) is : 4
print ("or, I can say (a*b).sum() is:", (a*b).sum())    #4
print ("This is a.dot(b):", a.dot(b))                   #4
print ("and this is b.dot(a):", b.dot(a))               #4
amag = np.sqrt((a*a).sum())                             # (1^2 + 2^2)^0.5 = 2.236067977
print ("Square root is:", amag)
cos_theta = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cos_theta)
print ("The angel (radian) bitween a and b:", angle)    #0.6435
print()

# Numpy Tutorials | 4. Vectors and Matrices: https://youtu.be/HycSKrideaM
M = np.array( [ [1, 2], [3, 4] ] )
L = [ [1, 2], [3, 4] ]
print ("L is:", L)                  #L is: [[1, 2], [3, 4]]
print ("L[0] is:", L[0])            #L[0] is: [1, 2]
print ("L[0][0] is:", L[0][0])      #L[0][0] is: 1

print ("M is:", M)                  #L is: [[1, 2], [3, 4]]
print ("M[0] is:", M[0])            #L[0] is: [1, 2]
print ("M[0][0] is:", M[0][0]) 
print  ()

# Ref: Numpy Tutorials | 5. Generating Matrices to Work With: https://youtu.be/AzIda9DL6i8
x = np.ones(11)
print ("A list have 11 ones.", x)   #[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
z = np.zeros( (5, 5) )
print ("A 5 * 5 matrix with all zeros.")
print (z)
print ()
R1 = np.random.random( (3, 3) )       #random.random --> 0 ~ 1
print (R1)
print ()
R2 = np.random.randn(3, 3)            #random.randn --> -1 ~ +1
print (R2)
print ()
print ("R2.mean() is:", R2.mean())      # 0.1976330053317371
print ("R2.var() is:", R2.var())        # 1.1306809161162341
print()


# Numpy Tutorials | 6. Matrix Products: https://youtu.be/g63QFedwP3E
# Numpy Tutorials | 7. More Matrix Operations: https://youtu.be/bjbIviyddS8
A = np.array( [ [1, 2], [3, 4] ]) 
A_inverse = np.linalg.inv(A)
print ("A_inverse is:")
print (A_inverse)
print ()
print ("Determine A is:", np.linalg.det(A))
print ("diag of A:", np.diag(A))
q = 3
w = 4 
e = 5
r = 6
print (np.diag([q, w, e, r]))

print ("Outer Product")
v_a = np.array([1, 2])
v_b = np.array([3, 4])
print ("Outer Product of a and b: ")
print (np.outer(v_a, v_b))
print ("Inner Product of a and b: ")
print (np.inner(v_a, v_b))

