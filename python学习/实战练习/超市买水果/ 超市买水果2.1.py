kind = int(input('要买几种水果？（一种输入1）'))
if kind == 1:
    type = int(input('你要买什么水果,有以下几种水果,1苹果,2香蕉,3橘子,4其他'))
    many = float(input('需要买多少斤'))
    fruit = dict(apple = 10,banana = 8,orange = 5)
    discount = int(input('有会员卡吗，有则输入1，无则输入0'))
    if discount == 1:
        discount =0.88
        if type == 1:
            print('你要买苹果')
            cost = (float(fruit['apple']) * discount * many)
            print(cost,'元')
        elif type == 2:
            print('你要买香蕉')
            cost = (float(fruit['banana']) * discount * many)
            print(cost,'元')
        elif type == 3:
            print('你要买橘子')
            cost = (float(fruit['orange']) * discount * many)
            print(cost,'元')
        else:
            new_fruit = str(input('你要买的水果是什么？'))
            new_fruit_cost = float(input('它的价格是多少？'))
            fruit[new_fruit] = new_fruit_cost
            cost = (float(fruit[new_fruit]) * discount * many)
            print(cost,'元')
    else:
        if type == 1:
            print('你要买苹果')
            cost = (float(fruit['apple']) * many)
            print(cost,'元')
        elif type == 2:
            print('你要买香蕉')
            cost = (float(fruit['banana']) * many)
            print(cost)
        elif type == 3:
            print('你要买橘子')
            cost = (float(fruit['orange']) * many)
            print(cost,'元')
        else:
            new_fruit = str(input('你要买的水果是什么？'))
            new_fruit_cost = float(input('它的价格是多少？'))
            fruit[new_fruit] = new_fruit_cost
            cost = (float(fruit[new_fruit]) * many)
            print(cost,'元')
else:
    kinds = kind
    fruits = dict()
    discount = int(input('有会员卡吗（有请输入1）'))
    all_many = dict()
    pre_cost = 0
    if discount == 1:
        discount = 0.88
        while len(fruits) < kinds:
            type = int(input('你要买什么水果,有以下几种水果,1苹果,2香蕉,3橘子,4其他'))
            if type == 1:
                print('你要买苹果')
                fruits['apple'] = 10
                many = float(input('你要买多少斤'))
                all_many['apple'] = many
            elif type == 2:
                print('你要买香蕉')
                fruits['banana'] = 8
                many = float(input('你要买多少斤'))
                all_many['banana'] = many
            elif type == 3:
                print('你要买橘子')
                fruits['orange'] =5
                many = float(input('你要买多少斤'))
                all_many['orange'] = many
            else:
                new_fruit = str(input('你要买的水果是什么？'))
                new_fruit_cost = float(input('它的价格是多少？'))
                fruits[new_fruit] = new_fruit_cost
                many = float(input('你要买多少斤'))
                all_many[new_fruit] = many
                print(fruits,all_many)
                pre_cost = (float(pre_cost) + float(fruits.get(new_fruit,0)) * float(all_many.get(new_fruit,0)))
                print(pre_cost)
        cost = (discount * (float(fruits.get('apple',0)) * float(all_many.get('apple',0)) + float(fruits.get('banana',0)) * float(all_many.get('banana',0)) + float(fruits.get('orange',0)) * float(all_many.get('orange',0)) + float(pre_cost)))
        print('一共',cost,'元')
    else:
        i = 0
        while i < kinds:
            type = int(input('你要买什么水果,有以下几种水果,1苹果,2香蕉,3橘子,4其他'))
            if type == 1:
                print('你要买苹果')
                fruits['apple'] = 10
                many = float(input('你要买多少斤'))
                all_many['apple'] = many
                i += 1
            elif type == 2:
                print('你要买香蕉')
                fruits['banana'] = 8
                many = float(input('你要买多少斤'))
                all_many['banana'] = many
                i += i
            elif type == 3:
                print('你要买橘子')
                fruits['orange'] =5
                many = float(input('你要买多少斤'))
                all_many['orange'] = many
                i += 1
            else:
                fruits.clear()
                all_many.clear()
                new_fruit = str(input('你要买的水果是什么？'))
                new_fruit_cost = float(input('它的价格是多少？'))
                fruits[new_fruit] = new_fruit_cost
                many = float(input('你要买多少斤'))
                all_many[new_fruit] = many
                pre_cost = ((float(pre_cost) + (float(fruits.get(new_fruit,0)) * float(all_many.get(new_fruit,0)))))
                i += 1
        cost = (float(fruits.get('apple',0)) * float(all_many.get('apple',0)) + float(fruits.get('banana',0)) * float(all_many.get('banana',0)) + float(fruits.get('orange',0)) * float(all_many.get('orange',0)) + float(pre_cost))
        print('一共',cost,'元')
