pi = 3.141592265

print(pi)

#변수에 저장된 값으로 연산하기

print(pi+2)
print(pi-2)
print(pi*2)
print(pi/2)
print(pi//2)
print(pi*pi)
print(pi%2)

#pi를 이용한 원의 둘레와 넓이 구하기
#파이썬은 변수를 사용할 때 
#변수의 자료형을 선언하지 않음
#그렇기 때문에 유연성이 생겨
#같은 변수에 여러가지 자료형을 넣을 수 있음!
#TypeError 발생할 수 있다

r = 10

print("원주율은 =",pi)
print("반지름 r = ",r)
print("원의 둘레 =",2*r*pi)
print("원의 넓이 =",r*r*pi)

#복합 대입 연산자 이용해보기

num = 100
num += 10
num += 20
num += 30
print(num)
# 160 출력!!
#문자열도 복합대입연산자 이용이 가능하다.

str = "안녕하세요"
str += "!"
str += "!"
print("str = ",str)
#안녕하세요!! 출력
# *= 문자열 반복 후 대입함
