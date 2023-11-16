import numpy as np
import matplotlib.pyplot as plt

import scipy

"""Simple iteration method"""
# x= 220
# i = 0
# xnew = 5
# diff = 5
# xnew_coll = [5]
# x_coll= [0]
# while diff>0.00000001:
#     xnew = np.sqrt(2*x + 8)
#     diff =  abs(xnew - x)
#     x = xnew
#     i +=1
#     xnew_coll.append(xnew)
#     x_coll.append(x)
#
#
#
# print(x)
# print(i)
#
#
# plt.plot(np.arange(i+1), xnew_coll)
# plt.plot(np.arange(i+1), x_coll)
# plt.show()

"""Newton Raphson method"""

# x = -5
# xnew = x - (2*x**2 - 5 * x  + 3) / (4 * x - 5)
#
#
# def fx(x):
#     return (x**2 + np.cos(x)**2  - 4 * x) / (2*(x - np.cos(x)* np.sin(x) - 2))
# for i in range(10000):
#     xnew = fx(x)
#     print('value after %d number of iterations %f' % (i, xnew))
#     if abs(x - xnew) < 0.0001:
#         break
#     x = xnew
#
# print(x)

"bisection method"
#
# x = -5
# def f(x):
#      return x**2 - 2 * x - 8
#
#
#
# x1 = 1
# x2 = +8
#
# while abs(x1 - x2) > 0.000001:
#
#      if f(x1) * f((x1 + x2)/2) < 0:
#           x2 = (x1 + x2) / 2
#
#      else:
#           x1 = (x1 + x2) / 2
#
# print(x1)


"""false position method"""

#
# def f(x):
#      return x**2 - 2 * x - 8
#
#
# x1 = 3
# x2 = +8
#
# diff = 0.5
# while abs(diff) > 0.0000000001:
#     xh = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
#     print('xh', xh)
#     print('x2', x2)
#     diff = xh - x2
#     x2 = xh
#
# print (x2)

"""secant method"""
# def f(x):
#     return x**2 - 2 * x - 8
#
# x1 = 3
# x2 = +5
#
# diff = 0.5
# while abs(diff) > 0.0000000001:
#     xh = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
#     print('xh', xh)
#     print('x2', x2)
#     diff = xh - x2
#     x1 = x2
#     x2 = xh
#
#
# print (x2)


# from scipy.optimize import newton, bisect,fsolve, root
#
# f = lambda x: x**2 - 2 * x - 8
#
# print(newton(f,0))
# print(newton(f,5))
#
#
# print(bisect(f,-5, 3))
#
# print(fsolve(f,[-1,-2,-3,0,1,2,3]))
#
# print(root(f, 0))



import numpy as np

# A = np.zeros([10,10])
#
# for i in np.arange(10):
#     for j in np.arange(10):
#         A[i,j] = np.random.randint(10, 50)
#
# print(A)

# np.linalg.solve(A,B)


x = [0,20,40,60,80,100]
y = [26,48.6, 61.6, 71.2, 74.8, 75.2]
#
# from scipy. interpolate import interp1d, lagrange
#
# f= interp1d(x,y,kind = 'cubic')
# print(f(50))
#
# L = lagrange(x,y)
# print(L)
# print(L(40))

# from scipy.stats import linregress
#
#
# L = linregress(x,y)
# print(L.slope, L.intercept)
#
# from scipy.optimize import curve_fit
#
# x = np.arange(6)
# y = [2, 8, 14, 28, 39, 62]
# def f(x, a0, a1, a2):
#     return a0 + a1*x + a2*x**2
#
# a,b = curve_fit(f,x,y)
# print(a)



"""Linear system solution in Numpy and Scipy"""
#
#
# A = np.zeros([10,10])
#
# for i in np.arange(10):
#     for j in np.arange(10):
#         A[i,j] = np.random.randint(10, 50)
#
# print(A.shape)
#
# B = np.ones([10,1])
# print(B.shape)
# for i in np.arange(10):
#     B[i,0] = np.random.randint(10, 50)
#
# print(np.linalg.solve(A,B))

"Differentiation"

# import scipy
#
# f =  lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
#
# h = 0.01
#
# x = np.linspace(0,1,11)
# dfc1 = scipy.misc.derivative(f,x,h,1)
# dfc2 = scipy.misc.derivative(f,x,h,2)
#
# plt.plot(x, f(x), '-k', x, dfc1, '--b', x, dfc2, '-.r')
# plt.xlabel('x')
# plt.ylabel('y, y\', y\'\'')
# plt.legend(['y', 'y\'', 'y\'\''])
# plt.show()


"""numeric integration"""

from scipy.integrate import *

# f = lambda x: x * np.sin(x)
#
# I = quad(f, 0, np.pi/2)
#
# print(I)
#
# fn = lambda x,y: y**2 * x + x**2 * y
# ax = 1; bx = 2
# ay = -1 ; by = 1
#
# print(dblquad(fn, ax, bx, lambda y:ay, lambda y: by))
#
# print(nquad(fn, [[ax, bx], [ay, by]]))


"""ordinary differential equations- euler"""

from math import exp


# dy = lambda x,y:x*y
# f = lambda x: exp(x**2/2)
#
# x = 0
# xn = 2
# y = 1
# h = 0.2
# n = int((xn-x)/h)
# print(n)
# x_coll = []
# y_coll_euler = []
# y_act = []
# for i in range(n):
#     y += dy(x,y) * h
#     x_coll.append(x)
#     y_act.append(f(x))
#     y_coll_euler.append(y)
#     x += h

#
#
#
# plt.plot(x_coll, y_coll_euler)
# plt.plot(x_coll, y_act)
# plt.show()




dy = lambda y,x : x * y

y0 = 1
x = np.linspace(0,2,5)
y = scipy.integrate.odeint(dy,y0,x) # y0 is initial valie





