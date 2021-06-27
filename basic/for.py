#range(A) 0 ~ A-1
#range(A, B) A ~ B-1
#range(A, B, C) A ~ B-1 / 앞뒤 숫자가 C 차이 만큼 가짐

#range(정수) 정수가 반드시 범위에 들어가야됨
#매개변수로 사용시 TypeError가 발생됨

for i in range(5):
    print(str(i) + "= 반복변수")
print()

for i in range(5, 10):
     print(str(i) + "= 반복변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "= 반복변수")
print()



array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번 째 반복 : {}".format(i, array[i])


#반대로 반복해보기
#역반복문
# 1
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수 : {}".format(i))


# 2
for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))
    