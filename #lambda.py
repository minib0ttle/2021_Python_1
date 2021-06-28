# lambda 
# lambda 매개변수 : 리턴값


power = lambda x : x * x
under_3 = lambda x : x < 3

list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("---map() 함수의 실행결과")
print("map(power, list_input_a) :",output_a)
print("map(power, list_input_a) :",list(output_a))
print()


#filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("---filter() 함수의 사용 ")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a): ",list(output_b))


list_input_b = [1, 2, 3, 4, 5]

output_a = map(lambda x : x * x, list_input_b)
print("map(power, list_input_a) :",output_a)
print("map(power, list_input_a) :",list(output_a))
print()


output_b = filter(lambda x : x < 3, list_input_b)
print("---filter() 함수의 사용 ")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a): ",list(output_b))

