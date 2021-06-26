string_num1 = input("입력A =")
int_num1 = int(string_num1)

string_num2 = input("입력B =")
int_num2 = int(string_num2)

print("입력 받은 문자열 : ",string_num1+string_num2)
print("INT형으로 변환된 자료형 : ",int_num1+int_num2)

#문자열 끼리 덧셈 연사자를 연결하면
#문자열 연결 연산자로
#숫자 끼리 덧셈 연산자로 연결하면
#숫자 덧셈 연산자로 이용


#int() 함수와 float() 함수 이용해보기

opt1 = int("23")
opt2 = float("22224.3142")

print(type(opt1))
print(type(opt2))

#class <int>와 <float> 출력

#int() 함수와 float() 함수 조합해서 이용해보기

input_1 = float(input("num 1 ="))
input_2 = float(input("num 2 ="))

print("덧셈 결과 = ",input_1 + input_2)
print("뺄셈 결과 = ",input_1 - input_2)
print("곱셈 결과 = ",input_1 * input_2)
print("나눗셈 결과 = ",input_1 / input_2)

#1. 변환할 수 없는 것을 변환하려고 하면
#ValueError 예외가 발생
#2. float형을 int형으로 변환할 때 
#에러 발생


#숫자를 문자열로 바꾸는 작업
#str() 함수를 이용해보기

output_1 = str(22)
output_2 = str(22.283)

print(type(output_1),output_1)
print(type(output_2),output_2)

#str 함수를 이용하면 숫자가 문자열로 바뀜
#그렇기 때문에 문자열을 이용한 연산도 가능하게 바뀌게 됩니다.
