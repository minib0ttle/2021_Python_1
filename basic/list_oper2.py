 #리스트 연결 연산자와 요소 추가의 차이
# 비파괴적 처리 

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)

# [1, 2, 3, 4, 5, 6]으로 출력
# but

print(list_a)
# [1, 2, 3]으로 출력
# 원형이 변하지 않는다.


list_a.extend([4, 5, 6])
print(list_a)
# 파괴적 함수 extend() 이용
# 원형이 변한다.

# 리스트의 요소를 제거하는 방법
# 1.인덱스로 제거하기
# 2.값으로 제거하기

# 1. del keyword, pop()
list_c = [0, 1, 2, 3, 4, 5, 6]
print("##리스트의 요소 하나 제거하기 ##")

del list_c[1]
print("del list_c[1] =",list_c)
# pop()함수에 요소가 들어가지 않으면
# 자동으로 -1이 입력되어 마지막 요소를 제거합니다.
list_c.pop(2)
print("list_c.pop(2) =",list_c)

# del [ : ]
list_d =[0, 1, 2, 3, 4, 5, 6]
del list_d[3 : 6] #마지막 요소 포함하지 않음
print(list_d)

list_d =[0, 1, 2, 3, 4, 5, 6]
del list_d[:3] #  3을 기준(3번째포함) 왼쪽의 요소 다 삭제
print(list_d)

list_d =[0, 1, 2, 3, 4, 5, 6]
del list_d[3:] #  3을 기준(3번째포함) 오른쪽 요소 다 삭제
print(list_d)

# 2. 값으로 제거하기
# remove() 함수 이용
# list.remove(value)

list_q = [1, 2, 1, 2]
list_q.remove(2) #왼쪽에서 부터 제일먼저 찾은 값이 2인 리스트 요소 삭제
print(list_q)
#반복문과 조합해서 구현도 가능

#모두제거하는 clear() 함수
#list.clear()

list_a.clear()
print(list_a)
#모두제거됨
#리스트안에 남아있는 요소가 없다.


