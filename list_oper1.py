list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("-----리스트 출력하기 -----")
print("list_a = ",list_a)
print("list_b = ",list_b)
print()

print("-----리스트 기본 연산자 -----")
print("list_a + list_b = ",list_a + list_b)
print("list_a * 3 = ",list_a * 3)
print() #\n과 같은 역할

#함수
print("-----길이 구하기 -----")
print("len(list_a) =", len(list_a))
print("len(list_b) =", len(list_b))



#리스트에 요소 추가하기
#append / insert

#list.append(element)
#list.insert(index, element)

print("----- 리스트 뒤에 요소 추가하기 -----")
list_a.append(4)
list_a.append(5)
list_a.append(6)
print()

print("----- 리스트 중간에 요소 추가하기 -----")
list_a.insert(0, 10) #0번 인덱스에 10을 추가하기
print(list_a) # 0번인덱스에 존재하고 있는 요소는 1번인덱스로 밀려남

#한번에 여러가지 요소를 추가하고 싶으면 extend() 함수를 이용한다.
#마치 extend는 append()함수를 3번 반복한 효과를 가져옴
#밑에 예제를 통해서 확인하면 3번 반복

list_a.extend([4, 5, 6])
print(list_a)
