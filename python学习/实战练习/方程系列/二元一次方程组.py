shizi01=input("你想要解的二元一次方程组中的第一个方程")#让用户写出方程
print("第一个方程为",shizi01)#重复输出
shizi02=input("第二个方程")#让用户写出方程
print("第二个方程为",shizi02)#重复输出
weizhishu01=input("方程中的第一个未知数")#让用户写出未知数
print("第一个为",weizhishu01)#重复输出
weizhishu02=input("方程中的第二个未知数")#让用户写出未知数
print("第二个为",weizhishu02)#重复输出
import sympy#引入数学模块
x=sympy.symbols(weizhishu01)#设未知数
y=sympy.symbols(weizhishu02)#设未知数
jieguo=sympy.solve([shizi01,shizi02],[x,y])#解方程
print(jieguo)#输出结果