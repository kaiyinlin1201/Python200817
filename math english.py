m=int(input("請輸入數學成績:"))
e=int(input("請輸入英文成績:"))

if (m>=0 and m<=100) and (e>=0 and e<=100):
    if (m>=90) and (e>=90):
        print("獲得獎品")
    elif (m<60) and (e<60):
        print("接受處罰!!!")
    elif (m>60) and (e<60):
        print("再加油")
    elif (m<60) and (e>60):
        print("再加油")
else:
    print("輸入錯誤")
