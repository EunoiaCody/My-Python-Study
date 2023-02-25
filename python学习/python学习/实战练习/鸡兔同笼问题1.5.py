head=int(input('有多少个头？'))#询问一共有多少个头
print('有',+head,'个头')#重复提示有多少个头
foot=int(input('有多少条腿？'))#询问一共有多少条腿
print('有',+foot,'条腿')#重复提示有多少条腿
full=head#头有多少和代表一共有多少只鸡和兔子
import sympy#引入数学模块sympy
x=sympy.symbols("x")#声明未知数x
a=sympy.solve((2*x+4*(+full-x))-foot)#列出式子
print('有',a,'只鸡')#输出结果：鸡的数量
b=sympy.solve(full-x)#求出兔子的数量
print('有',b,'只兔子')#输出结果：兔子的数量