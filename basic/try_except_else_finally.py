try :
    number_input = int(input("정수 입력하세요 :"))
    
    print("원의 반지름 :",number_input)
    print("원의 넓이 :", 3.14 * number_input * number_input)
    print("원의 둘레 :", 2 * 3.14 *number_input)

    
    
except :
    print("정수를 입력하지 않았습니다.")

else :
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 끝났습니다.")



    