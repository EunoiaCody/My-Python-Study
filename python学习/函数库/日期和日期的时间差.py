import datetime
birthday = datetime.date(
    year=int(input("请输入你生日的年份:")),
    month = int(input("请输入你生日的月份:")),
    day = int(input("请输入你生日的日期:")),
)
today = datetime.date.today()
age = round((today-birthday).days/365,1)
print(age)