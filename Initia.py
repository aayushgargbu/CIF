# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:14:25 2019

@author: AG
"""

#from Timer import Timer
#import random

def NewtonRaphsonSqRt(x):
    # works for at max 10,000,000
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        #print("approx:",approx)
        approx = guess
        guess = (approx + x / approx) / 2
    assertCheck(approx * approx, x)
    return approx
        

def assertCheck(num1, num2, EPSILON = 1e-8):
    try:
        assert abs(num1-num2) < EPSILON
    except Exception:
        print('Exception:',num1, num2)

#sqNum = int(input('Please enter number to find its square root:'))
sqNum = 9
#print('Square root of number', sqNum,'is:',NewtonRaphsonSqRt(sqNum))
sqRoot = 3

#if NewtonRaphsonSqRt(sqNum) == sqRoot:
#    print('Passed')
#else:
#    print('Failed')

#Gives AssertionError
assert NewtonRaphsonSqRt(sqNum) == sqRoot

assertCheck(NewtonRaphsonSqRt(9), 3)
assertCheck(NewtonRaphsonSqRt(4), 2)

assertCheck(NewtonRaphsonSqRt(.3) * NewtonRaphsonSqRt(.3), .3)

# =============================================================================
# with Timer() as t:
# #for n in (1, 10000000000):
#     for i in range(10000):
#         n = 1 + random.random() * 10000000
#         sqRootOfn = NewtonRaphsonSqRt(n)
#         #assertCheck(sqRootOfn * sqRootOfn, n)
# print('Time taken:', t.elapsed_time())
# =============================================================================

def GetSquareRoot(usrInpt):
    try:
        sqrNum = float(usrInpt)
    except ValueError:
        print('Only Numbers Please')
    else:
        if sqrNum < 0:
            print('Only Non-Negative Numbers Please')
        elif sqrNum == 0:
            print('Square root of number', sqrNum,'is:', 0)
        else:
            print('Square root of number', sqrNum,'is:', NewtonRaphsonSqRt(sqrNum))

sqNum = input('Please enter number to find its square root:')
GetSquareRoot(sqNum)