# format() 함수는 숫자를 문자열로 변환시킬 수 있음.
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