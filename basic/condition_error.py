user_input = input("정수입력:")

if user_input.isdigit():
    number_input = int(user_input)

    print("원의 반지름 :",number_input)
    print("원의 둘레 :", 2 * 3.14 * number_input)
    print("원의 넓이 :", 3.14 * number_input * number_input)

else :
    print("정수를 입력하지 않았습니다.")

