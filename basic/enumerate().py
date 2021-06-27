example_list = ["요소A", "요소B", "요소C"]

print("---단순출력")
print(example_list)
print()

print("---enumerate() 함수 사용 :")
print(enumerate(example_list))
print()

print("#list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("---반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value)



ex_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}


print("---딕셔너리의 items() 함수")
print("items() :", example_dictionary.items())
print()

print("---딕셔너리의 items() 함수와 반복문 조합하기")


for key, element in ex_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
    


