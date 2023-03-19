number=int(input("你要买几种水果？（一种输入1，以此类推）"))
if number==1:
    i=1
    while i > 0:
        type=int(input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）"))
        i = i - 1
    if type==1:
        print("你买了苹果")
        many=int(input("你要买几斤"))
        cost=many*10
        print("你买了苹果",many,"斤，花费",cost,"元")
    elif type==2:
        print("你买了香蕉")
        many=int(input("你要买几斤"))
        cost=many*8
        print("你买了香蕉",many,"斤，花费",cost,"元")
    elif type==3:
        print("你买了荔枝")
        many=int(input("你要买几斤"))
        cost=many*6
        print("你买了荔枝",many,"斤，花费",cost,"元")
    elif type==4:
        print("你买了葡萄")
        many=int(input("你要买几斤"))
        cost=many*5
        print("你买了葡萄",many,"斤，花费",cost,"元")
    elif type==5:
        print("你买了草莓")
        many=int(input("你要买几斤"))
        cost=many*4
        print("你买了苹果",many,"斤，花费",cost,"元")
    else:
        print("此水果本店不买")
elif number==2 or 3 or 4 or 5:
    i = number
    if i == 1:
        while i > 0:
            type=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
    elif i == 2:
        while i > 0:
            type_1=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_2=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
    elif i == 3:
        while i > 0:
            type_1=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_2=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_3=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
    elif i == 4:
        while i > 0:
            type_1=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_2=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_3=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_4=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
    elif i == 5:
        while i > 0:
            type_1=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_2=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_3=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_4=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1
            type_5=input("你要买哪些水果？（苹果1，香蕉2，荔枝3，葡萄4，草莓5）")
            i = i - 1