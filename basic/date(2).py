import datetime

now = datetime.datetime.now()
#datetime을 이용한
#오전 오후로 나누기

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다 ! ".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다 !".format(now.hour))


#datetime을 이용한 
#계절 출력하기

#봄 구분
if 3<=now.month <= 5:
    print("이번 달은 {}월로 봄입니다 !".format(now.month))
#여름 구분
if 6<=now.month <= 8:
    print("이번 달은 {}월로 여름입니다 !".format(now.month))
#가을 구분
if 9<=now.month <= 11:
    print("이번 달은 {}월로 가을입니다 !".format(now.month))
#겨울 구분
if now.month == 12 or 1<=now.month <=2 :
    print("이번 달은 {}월로 겨울입니다 !".format(now.month))