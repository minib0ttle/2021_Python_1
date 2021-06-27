def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()


def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 5)

#variable_parameter

def print_x_times(n, *values):
    #n번 반복하기
    for i in range(n):
        for value in values:
            print(value)
        print()

    

