str = input("인사말을 입력해보세요 :")
#input() 함수는
#프로그램이 잠시 멈추도록
#코드진행을 block하고 있음.
print(str)

#input() 함수의 결과는 리턴값이라고 부름

num = input("숫자를 입력해보세요")
print(num)

print(type(str))
print(type(num))

#두 개의 input()함수의 결과는 둘 다
#str 타입이라고 나옴
#무조건 문자열 자료형

print("num + 100 = ",num+100)
#오류 발생
#input()으로 받은 num 변수는 문자열이기 때문에
#숫자와 연산하려고 하면 TypeError 발생

