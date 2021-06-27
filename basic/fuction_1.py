def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
#3번 반복

def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 5)

# variable_parameter
# 가변매개변수사용하기
# 뒤에 일반매개변수사용 불가능
# 함수내에서 하나만 사용가능
# *values -> 가변매개변수로 선언

def print_x_times(n, *values):
    #n번 반복하기
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

# 가변매개변수는 리스트처럼 사용가능


# ------------기본매개변수
# 매개변수 = 값 형태로 되어있음
# 기본매개변수 뒤에는 일반 매개변수가 올 수 없음.
def print_y_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)

# 함수를 호출합니다.

print_y_times("안녕하세요")
    

