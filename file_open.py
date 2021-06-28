file = open("basic.txt", "w")

file.write("Hello World!")

file.close()


#close()를 잊어버리고 프로그램을 종료하는 일이 있음
# with 키워드를 사용하면 프로그램 종료시 자동으로 닫음

with open("basic_2.txt","w") as file:
    file.write("Hello World!")

# 텍스트 읽기
# read()

with open("basic.txt","r") as file:
    contents = file.read()

print(contents)

