#min()
#max()
#sum()



numbers = [103, 52, 273, 32, 77]

#리스트 내부에서 최솟값 찾기
min(numbers)

#리스트 내부에서 최댓값 찾기
max(numbers)

#리스트 내부에서 값을 모두 더하기
sum(numbers)

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("--- reversed() 함수")
print("reversed[1,2,3,4,5] =",list_reversed)
 #오류 발생 - reversed() 함수의 결과가 제너레이터 이기 때문

print("list(reversed(list_a)) =",list(list_reversed))
print()


print("--- reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]) =")
for i in reversed(list_a):
    print(" - ",i)

#확장 슬라이싱을 통한 리스트 내용 뒤집기

numbers[::-1]

print(numbers[::-1])
