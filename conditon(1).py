number = input("일반 정수 입력 :")


#끝 자리 숫자만 추출
last_num = number[-1]
last_num = int(last_num)

if last_num == 0 \
    or last_num == 2 \ 
    or last_num == 4 \ 
    or last_num == 6 \ 
    or last_num == 8 :
    print("짝수입니다")

if last_num == 1 \
    or last_num == 3 \
    or last_num == 5 \
    or last_num == 7 \
    or last_num == 9 :
    print("홀수입니다")


#in연산자 이용해서 홀수, 짝수 구분하기
if last_num in "02468" :
    print("짝수입니다")

if last_num in "13579" :
    print("홀수입니다")


#나머지를 확인하여 구분하는 방법 
#나머지연산자 % 이용

if number % 2 ==0:
    print("짝수입니다")

if number % 2 == 1:
    print("홀수입니다")


if number % 2 == 0:
    print("짝수입니다")

else :
    print("홀수입니다")
    