# 기본 매개변수 중에서 필요한 값만 입력하기

def test(a, b=10, c=100):
    print(a+b+c)
# a는 일반매개변수
# b와 c는 기본매개변수

# 기본형태
test(10, 20, 30)

# 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)

# 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b= 200)

# 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)

# return

# 자료 없이 리턴하기

def return_test():
    print("A의 위치입니다.")
    return
    print("B의 위치입니다.")

return_test()

# 자료와 함께 리턴하기
def return_exe():
    return 100

value = return_exe()
print(value)

# 아무것도 리턴하지 않기

def return_emp():
    return

value = return_emp()
print(value)

# None 출력
# '아무것도 없다'를 의미함.

def sum_all_ver1(start, end):
    output =0
    for i in range(start, end+1):
        output += i
    return output

print("0 ~ 100 sum = ",sum_all(0,100))

def sum_all_ver2(start=0, end=100, step =1):
    output =0
    for i in range(start, end+1, step):
        output += i
    return output

print("A.", sum_all_ver2(0, 100, 10))
print("B.", sum_all_ver2(end=100))
print("C.", sum_all_ver2(end=100 ,step=2))



