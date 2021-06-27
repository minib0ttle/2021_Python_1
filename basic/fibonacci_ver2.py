count = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter #UnboundLocalError global 키워드 사용
    counter +=1

    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수 는 {]번 입니다.".format(counter))

