# break문 활용하기

i = 0

while True :
    print("{}번째 반복입니다 .".format(i))
    i = i+1
    input_text = input("종료하시려면 y를 입력하세요 :")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break

# continue문 활용하기

numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)
