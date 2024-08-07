# -*- coding: utf-8 -*-

fruits = {'苹果': 10, '香蕉': 8, '橘子': 5}
total_weight = 0
total_price = 0

# 询问用户想买哪些水果
order = input("你想买哪些水果？（以空格分隔，例如'苹果 香蕉'）").split()

# 遍历用户的订单，计算每个水果的数量和价格
for item in order:
  if item in fruits:
    kg = float(input(f"你要买多少千克{item}？"))
    total_weight += kg
    total_price += kg * fruits[item]

  # 用户想买的水果不在预设列表中，则询问水果名称和单价
  else:
    fruit_name = input("这种水果叫什么名字？")
    fruit_price = float(input("这种水果每千克多少钱？"))
    kg = float(input(f"你要买多少千克{fruit_name}？"))
    total_weight += kg
    total_price += kg * fruit_price

# 询问用户是否是会员
is_member = input("你是会员吗？（是/否）") == "是"

# 计算优惠后的价格
final_price = total_price / 2 if is_member else total_price

# 输出订单信息
print(f"你一共买了 {total_weight:.2f} 千克水果")
print(f"你一共需要支付 {final_price:.2f} 元")


#
# 输出订单信息
print(f"你一共买了 {total_weight:.2f} 千克水果")
print(f"你一共需要支付 {final_price:.2f} 元")


#这个程序首先定义了一个字典 fruits， Key为水果名称， Value为每千克的价格。接着通过 input() 函数询问用户想买哪些水果。如果用户需要买的水果在预设列表中，程序会再次通过 input() 函数询问用户想买多少千克，然后累加订单的总重量和总价。如果用户需要买的水果不在预设列表中，则会询问用户水果名称和单价，然后计算总重量和总价。

#然后程序会询问用户是否是会员，通过 input() 函数获得答案，如果是会员则打折 50%。最后输出订单的信息：总重量和最终需要支付的金额。

