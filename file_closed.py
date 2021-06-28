try :
    file = open("info.txt","w")

    file.close()
except Exception as e:
    print(e)
print("파일이 제대로 닫혔는지 확인하기")
rpint("file closed : ",file.closed)




# try 구문 도중에 오류가 발생하면
# 실행 도중에 종료하게 된다
# 그러므로 2가지 정도 방법이 있다.




# finally :
#   file.close()



# try-except 구문 끝난 후
# file.close() 호출하기

