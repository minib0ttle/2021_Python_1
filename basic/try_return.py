def test():
    print("test() 함수의 첫 줄입니다.")
    try :
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    
    except :
        print("except 구문이 실행되었습니다.")

    else :
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

test()


# finally 키워드 이용하기

def write_text_file(filename, text) :
    try:
        file = open(filename, "w")
        return
        file.write(text)
    
    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "안녕하세요 !")
