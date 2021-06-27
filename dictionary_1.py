# ex >> for i in range(100)
array = [273, 32, 103, 57, 52]

# 리스트에 반복문을 적용하기

for element in array :
    print(element)

#dictionary define
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "orgin" : "필리핀"
}

print("name :", dictionary["name"])
print("type :", dictionary["type"])
print("ingredient :", dictionary["ingredient"])
print("ingredient :", dictionary["ingredient"][1]) #설탕 출력
print("orgin :", dictionary["orgin"])
print()


#딕셔너리 요소 값 변경하기
dictionary["name"] = "8D 건조 망고"
print("name :", dictionary["name"])

#딕셔너리 NameError
"""
    dict_key = {
        name : "7D 건조 망고"
        type : "당절임"
    }
"""

#dictionary 에 값 추가 / 제거 하기
dictionary["price"] = 5000  #추가됨
print(dictionary)

del dictionary["ingredient"]
print(dictionary)


dic = {}
print("요소 추가 이전 : ",dic)

dic["name"] = "나다"
dic["price"] = 50000
dic["body"] = "몸이다"

print("요소 추가 이후 : ",dic)

#제거해보기

del dic["name"]
print("name 제거 : ",dic)

del dic["price"] 
print("price 제거 : ",dic)

#KeyError
#딕셔너리에 없는 값에 접근을 하면 KeyError 발생


#딕셔너리 in keyword 
#dictionary define
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "orgin" : "필리핀"
}

key = input(" 접근하고싶은 키 :")

if key in dictionary:
    print(dictionary[key])
else :
    print("존재하지 않은 키에 접근하고 있음.")
    print("KeyError")



#get() 함수 이용하기

value = dictionary.get("존재하지 않는 키")
print("값 : ",value)

if value == None:
    print("존재하지 않는 키에 접근하였습니다.")

#for문과 딕셔너리

for i in dictionary:
    print(key, ":", dictionary[key])
