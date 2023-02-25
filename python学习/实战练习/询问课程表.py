import datetime
import time
import calendar
Qtype=int(input("通过日期（今天）或是星期（几）（选择日期请输入1，星期则是2）"))
if Qtype==1:
    classtype=int(input("获取今天的，指定日期的（分别输入1，2）"))
    if classtype==1:
        today=datetime.date.today()
        weekday_1=int(format(today.weekday()))
        weekday_1=int(weekday_1+1)
        if weekday_1==1:
            print(
                "今天是星期一，课程如下：",
                "英语",
                "地理",
                "英会话",
                "体育",
                "数学",
                "数学",
                "语文",
                "班会"
            )
        elif weekday_1==2:
            print(
                "今天是星期二，课程如下：",
                "语文",
                "历史",
                "英语",
                "英语",
                "美术",
                "数学",
                "物理",
                "生物"
            )
        elif weekday_1==3:
            print(
                "今天是星期三，课程如下：",
                "数学",
                "数学",
                "音乐",
                "体育",
                "英语",
                "道法",
                "语文",
                "生物"
            )
        elif weekday_1==4:
            print(
                "今天是星期四，课程如下：",
                "物理",
                "历史",
                "体育",
                "语文",
                "英语",
                "数学",
                "电脑",
                "地理"
            )
        elif weekday_1==5:
            print(
                "今天是星期五，课程如下：",
                "数学",
                "道法",
                "语文",
                "语文",
                "生物",
                "物理",
                "英语",
                "英语"
            )
        elif weekday_1==6 or 7:
            print("今天是周末，没有课")
    elif classtype==2:
        date=datetime.date(
            year=int(input("公元几年？")),
            month=int(input("几月？")),
            day=int(input("几号？"))
        )
        weekday_2=int(format(date.weekday()))
        if weekday_2==1:
            print(
                "今天是星期一，课程如下：",
                "英语",
                "地理",
                "英会话",
                "体育",
                "数学",
                "数学",
                "语文",
                "班会"
            )
        elif weekday_2==2:
            print(
                "今天是星期二，课程如下：",
                "语文",
                "历史",
                "英语",
                "英语",
                "美术",
                "数学",
                "物理",
                "生物"
            )
        elif weekday_2==3:
            print(
                "今天是星期三，课程如下：",
                "数学",
                "数学",
                "音乐",
                "体育",
                "英语",
                "道法",
                "语文",
                "生物"
            )
        elif weekday_2==4:
            print(
                "今天是星期四，课程如下：",
                "物理",
                "历史",
                "体育",
                "语文",
                "英语",
                "数学",
                "电脑",
                "地理"
            )
        elif weekday_2==5:
            print(
                "今天是星期五，课程如下：",
                "数学",
                "道法",
                "语文",
                "语文",
                "生物",
                "物理",
                "英语",
                "英语"
            )
        elif weekday_2==6 or 7:
            print("今天是周末，没有课")
elif Qtype==2:
    weekday_3=int(input("今天星期几？（周一输入1，以此类推）"))
    if weekday_3==1:
        print(
            "今天是星期一，课程如下：",
            "英语",
            "地理",
            "英会话",
            "体育",
            "数学",
            "数学",
            "语文",
            "班会"
        )
    elif weekday_3==2:
        print(
            "今天是星期二，课程如下：",
            "语文",
            "历史",
            "英语",
            "英语",
            "美术",
            "数学",
            "物理",
            "生物"
        )
    elif weekday_3==3:
        print(
            "今天是星期三，课程如下：",
            "数学",
            "数学",
            "音乐",
            "体育",
            "英语",
            "道法",
            "语文",
            "生物"
        )
    elif weekday_3==4:
        print(
            "今天是星期四，课程如下：",
            "物理",
            "历史",
            "体育",
            "语文",
            "英语",
            "数学",
            "电脑",
            "地理"
        )
    elif weekday_3==5:
        print(
            "今天是星期五，课程如下：",
            "数学",
            "道法",
            "语文",
            "语文",
            "生物",
            "物理",
            "英语",
            "英语"
        )
    elif weekday_3==6 or 7:
        print("今天是周末，没有课")