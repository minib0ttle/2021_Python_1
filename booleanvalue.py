#참과 거짓을 나타내는
#Boolean값
print(True)
print(False)

#비교연산자를 통한 Boolean값 생성
# ==, >, >=, <, <=, !=

print(10 == 10)
print(10 > 10)
print(10 >= 10)
print(10 < 10)
print(10 <= 10)
print(10 != 10)

#문자열도 비교연산자 사용가능!
#문자열은 사전 순서대로 계산
#사전에 앞에있는 단어라면 숫자가 작음

print("호랑이" == "호랑이")
print("호랑이" != "사자")
print("나무" < "나라")
print("가방" > "하마")


#범위구하기
x =25
print(10<x<30) #true
print(40<x<50) #false

#불 연산 : 논리연산자
# not / and / or

#not
#단항연산자
print(not True)
print(not False)

#not 연산자 조합
x = 10
under_x = x<20
print("under_x = ",under_x)
print("not under_x =",not under_x)

#and 와 or 연산자

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)


