# 메모 변수를 이용

dictionary = {
    1 : 1,
    2 : 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else :
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print("fibonacci(10): ", fibonacci(10))
print("fibonacci(20): ", fibonacci(20))
print("fibonacci(30): ", fibonacci(30))
print("fibonacci(40): ", fibonacci(40))
print("fibonacci(50): ", fibonacci(50))

# 딕셔너리를 사용해서 한 번 계산값을 메모함 
# 메모화를 사용하면 속도가 빨라짐
# 쓸모없는 계산을 할 필요가 없음.