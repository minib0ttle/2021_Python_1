#false로 자동변환되는 값

if 0 :
    print("0은 True로 변환되는 값이다.")
    print("0은 False로 변환되는 값이다.")

if "" :
    print("빈 문자열은 True로 변환되는 값이다.")

else :
    print("빈 문자열은 False로 변환되는 값이다.")

#Pass KeyWord
#IndentationError

number = input("정수를 입력하세요 :")
number = int(number)

if number > 0 :
    #아직 미구현
    pass

else :
    #아직 미구현
    pass


"""
raise NotImplementError
강제로 에러를 발생시킨다.
if number > 0 :
   raise NotImplementError
else :
   raise NotImplementError
"""