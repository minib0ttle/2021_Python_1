# 무한반복
# while True :

# while 구조
# while 불 표현식 :
#   문장


i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1


list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_test.remove(2)

print(list_test)

#유닉스 타임
import time
number = 0

target_tick = time.time() + 5
while time.time() < target_tick :
    number += 1

print("5초 동안 {}번 반복했습니다 .".format(number))



