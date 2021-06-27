import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")


#format() 함수 이용
print("--------------------")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,
now.month, now.day, now.hour, now.minute, now.second))