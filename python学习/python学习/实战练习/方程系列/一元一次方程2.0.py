shizi=input("输入你想解的方程")
print("式子为",shizi)
weizhishu=input("输入方程所有的未知数")
import sympy
print("未知数为",weizhishu)
x=sympy.symbols(weizhishu)
print("结果为",sympy.solve([shizi],[x]))
print(" ")
again=int(input("需要再解一题吗？需要请输入1，不需要请输入0"))
while again==1:
    print(" ")
    shizi=input("输入你想解的方程")
    print("式子为",shizi)
    weizhishu=input("输入方程所有的未知数")
    import sympy
    print("未知数为",weizhishu)
    x=sympy.symbols(weizhishu)
    print("结果为",sympy.solve([shizi],[x]))
    again=input("需要再解一题吗？需要请输入1，不需要请输入0.")
    if again==0:
        break