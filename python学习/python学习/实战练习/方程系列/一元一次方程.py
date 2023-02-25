shizi=input('你想要解的方程(以x为未知数)')#让用户写出方程
import sympy#引入数学模块
x=sympy.symbols("x")#设未知数
a=sympy.solve(shizi,[x])#解方程
print(a)#输出方程的解