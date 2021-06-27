# format() 함수는 숫자를 문자열로 변환시킬 수 있음.
from _typeshed import OpenTextMode


str_a = "{}".format(10)
str_b ="{} {}".format(10,20)
str_c = "{} {} {} {}".format(10,20,30,40)

print(str_a)
print(type(str_a))
print("-----------")

print(str_b)
print(type(str_b))
print("-----------")

print(str_c)
print(type(str_c))
print("-----------")

# format() 함수의 여러가지 형태
format_1 = "{}만 원".format(24)
format_2 = "파이썬 열공하여 첫 연봉 {}만원 받기".format(8000)
format_3 = "{}과 {}과 {}".format(100,200,300)
format_4 = "숫자 = {}, 문자열 = {}, boolean = {}".format(1,"문자열",True)

print(format_1)
print(format_2)
print(format_3)
print(format_4)
# 숫자를 문자열로 바꾸었으니 
# string 타입으로 나와야함.

print(type(format_1))
print(type(format_2))
print(type(format_3))
print(type(format_4))

#IndexError 
#{}기호의 개수가 format()함수의 매개변수 개수 보다 많으면 발생!

#"{} {}".format(1,2,3,4,5)
#'1,2'만 출력되고 나머지 매개변수는 버려집니다.

#"{} {} {}".format(1,2)
# error 발생

#"{} {} {}".format(1,2)
# error 발생

#정수를 특정 칸에 출력해보기

output_a = "{:d}".format(12)
output_b = "{:5d}".format(12)
output_c = "{:10d}".format(12)

output_d = "{:05d}".format(100)
output_e = "{:05d}".format(-100)

print("-----------basic output-----------")
print(output_a)
print("특정칸에 출력하기")
print(output_b)
print(output_c)
print("빈칸을 0으로 채우기")
print(output_d)
print(output_e)

#기호 붙여 출력해보기

output_f = "{:+d}".format(12)
output_g = "{:+d}".format(-12)
#기호 부분 공백
#output_h = "{: d}".format(12)
#output_i = "{: d}".format(-12)

print("기호와 함께 출력해보기")
print(output_f)
print(output_g)


# 종합
#기호를 뒤로 밀기
output_h = "{:+5d}".format(12)
output_i = "{:+5d}".format(-12)
#기호를 앞으로 밀기
output_j = "{:=+5d}".format(12)
output_k = "{:=+5d}".format(-12)
#기호를 앞으로 공백은 0으로 채우기
output_l = "{:+05d}".format(12)
output_m = "{:+05d}".format(-12)


print("조합해보기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
