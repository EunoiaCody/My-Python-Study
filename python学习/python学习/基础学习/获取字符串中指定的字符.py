IdentityCode=input("请输入你的身份证号")
birthday=IdentityCode[6:14]
BirthdayYear=birthday[0:4]
BirthdayMonth=birthday[4:6]
BirthdayDay=birthday[6:8]
print("你的生日是")
print(BirthdayYear,BirthdayMonth,BirthdayDay,sep="-")
sex=int(IdentityCode[16])
if sex%2==0:
    print("你是一位女性")
else:
    print("你是一位男性")