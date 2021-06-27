import datetime

now = datetime.datetime.now()
month = now.month



#봄 구분
if 3<=month <= 5:
    print("현재는 봄입니다.")
#여름 구분
else if 6<=month <= 8:
    print("현재는 여름입니다.")
#가을 구분
else if 9<=month <= 11:
    print("현재는 가을입니다.")
#겨울 구분
else :
    print("현재는 겨울입니다.")