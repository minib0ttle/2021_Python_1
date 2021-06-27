#find()
#rfind()
#문자열 내부에 특정 문자가 어디에 위치하고 있는지 확인
#find() - 왼쪽부터 찾아서 처음 등장하는 위치 반환
#rfind() - 오른쪽부터 찾아서 처음 등장하는 위치 반환

output_a = "안녕안녕하세요".find("안녕")
print(output_a)
#결과값은 0

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
#결과값은 2
#인덱스 반환

#문자열 내부의 어떠한 문자열이 있는지 
#in연산자 활용하기
#출력 boolean값

output_c = "안녕하세요"
print("안녕" in output_c)
#true

print("안녕" in output_c)
#false

#문자열 자르기
#split() 활용하기
#문자열을 특정한 문자로 자를 때 활용

input_a = "1 2 3 4 5 ".split(" ")
#공백을 기준으로 문자열 자르기

print(input_a)
#실행결과는 리스트 나옴
