# try : 
# 예외가 발생할 가능성이 있는 코드

# except :
# 에외가 발생했을 때 실행할 코드



try :
    number_input = int(user_input(" 정수 입력 :"))


    print("원의 반지름 :",number_input)
    print("원의 둘레 :", 2 * 3.14 * number_input)
    print("원의 넓이 :", 3.14 * number_input * number_input)

except :
    print("무언가 잘못되었습니다.")



# pass 키워드 이용하기
# 숫자로 변환되는 것들만 리스트에 넣기

list_input = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input:
    try :
        float(item)
        list_number.append(item)

    except:
        pass


print("{} 내부에 있는 숫자는".format(list_input))
print("{} 입니다.".format(list_number))