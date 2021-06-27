# 반복문으로 팩토리얼 구하기

def factorial_for(n):
    output =1
    for i in range(1, n+1)
        output *= i
    
    return output

print("1! :", factorial_for(1))
print("2! :", factorial_for(2))
print("3! :", factorial_for(3))
print("4! :", factorial_for(4))
print("5! :", factorial_for(5))

# 재귀함수를 이용해서 팩토리얼 구하기

def factorial_recur(n):
    if n==0:
        return 1
    else :
        return n * factorial_recur(n-1)


print("1! :",factorial_recur(1))
print("2! :",factorial_recur(2))
print("3! :",factorial_recur(3))
print("4! :",factorial_recur(4))
print("5! :",factorial_recur(5))
