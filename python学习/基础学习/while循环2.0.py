type=int(input("一元一次方程，二元一次方程组或是三元一次方程组（请输入1，2或3）"))
if type==1:
    shizi=input("输入你想解的方程")
    print("式子为",shizi)
    weizhishu=input("输入方程所有的未知数")
    import sympy
    print("未知数为",weizhishu)
    x=sympy.symbols(weizhishu)
    print("结果为",sympy.solve([shizi],[x]))
elif type==2:
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
elif type==3:
    shizi01=input("你想要解的三元一次方程组中的第一个方程")#让用户写出方程
    print("第一个方程为",shizi01)#重复输出
    shizi02=input("第二个方程")#让用户写出方程
    print("第二个方程为",shizi02)#重复输出
    shizi03=input("第三个方程")#让用户写出方程
    print("第三个方程为",shizi03)#重复输出
    weizhishu01=input("方程中的第一个未知数")#让用户写出未知数
    print("第一个为",weizhishu01)#重复输出
    weizhishu02=input("方程中的第二个未知数")#让用户写出未知数
    print("第二个为",weizhishu02)#重复输出
    weizhishu03=input("方程中的第三个未知数")#让用户写出未知数
    import sympy#引入数学模块
    x=sympy.symbols(weizhishu01)#设未知数
    y=sympy.symbols(weizhishu02)#设未知数
    z=sympy.symbols(weizhishu03)#设未知数
    jieguo=sympy.solve([shizi01,shizi02,shizi03],[x,y,z])#解方程
    print(jieguo)#输出结果
again=input("需要再解一题吗？（是请输入1，否请输入0)")
while again==1:
    type=int(input("一元一次方程，二元一次方程组或是三元一次方程组（请输入1，2或3）"))
    if type==1:
        shizi=input("输入你想解的方程")
        print("式子为",shizi)
        weizhishu=input("输入方程所有的未知数")
        import sympy
        print("未知数为",weizhishu)
        x=sympy.symbols(weizhishu)
        print("结果为",sympy.solve([shizi],[x]))
    elif type==2:
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
    elif type==3:
        shizi01=input("你想要解的三元一次方程组中的第一个方程")#让用户写出方程
        print("第一个方程为",shizi01)#重复输出
        shizi02=input("第二个方程")#让用户写出方程
        print("第二个方程为",shizi02)#重复输出
        shizi03=input("第三个方程")#让用户写出方程
        print("第三个方程为",shizi03)#重复输出
        weizhishu01=input("方程中的第一个未知数")#让用户写出未知数
        print("第一个为",weizhishu01)#重复输出
        weizhishu02=input("方程中的第二个未知数")#让用户写出未知数
        print("第二个为",weizhishu02)#重复输出
        weizhishu03=input("方程中的第三个未知数")#让用户写出未知数
        import sympy#引入数学模块
        x=sympy.symbols(weizhishu01)#设未知数
        y=sympy.symbols(weizhishu02)#设未知数
        z=sympy.symbols(weizhishu03)#设未知数
        jieguo=sympy.solve([shizi01,shizi02,shizi03],[x,y,z])#解方程
        print(jieguo)#输出结果
    elif again==0:
        break
