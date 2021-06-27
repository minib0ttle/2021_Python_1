# 튜플은 한번 결정된 요소를 바꿀 수 없다.
#(데이터 , 데이터 , ---)


[a, b] = [10, 20]
(c, d) = (10, 20)

print("a :",a)
print("b :",b)
print("c :",c)
print("d :",d)

tuple_test = 10,20,30,40
print("괄호가 없는 튜플 값과 자료형 출력해보기")
print("tuple_test :",tuple_test)
print("type(tuple_test) :",type(tuple_test))
print()


d, e, f = 10, 20, 30

print("괄호가 없는 튜플을 활용한 할당")
print("d :",d)
print("e :",e)
print("f :",f)

x, y = 10, 20

print("교환 전의 값")
print("x :",x)
print("y :",y)
print()

x, y = y, x

print("교환 후의 값")
print("x :",x)
print("y :",y)
print()

# 튜플을 여러개의 값을 리턴하기 위해서 자주 이용함

def test():
    return (10, 20)

m, n =test()
print("m :",m)
print("n :",n)
