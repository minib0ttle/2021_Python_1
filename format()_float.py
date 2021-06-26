#기본출력
from _typeshed import OpenTextMode


output_a = "{:f}".format(72.683)
#15칸 생성
output_b = "{:15f}".format(72.683)
#15칸생성과 부호붙이기
output_c = "{:+15f}".format(72.683)
#15칸생성과 부호붙이고 0으로 채우기
output_d = "{:+015f}".format(72.683)

print(output_a)
print(output_b)
print(output_c)
print(output_d)

#소수점 아래 자릿수 지정해보기
output_e = "{:15.3f}".format(72.683)
output_f = "{:15.2f}".format(72.683)
output_g = "{:15.1f}".format(72.683)

print(output_e)
print(output_f)
print(output_g)

#의미없는 소수점 제거하기
output_h = 72.0
output_i = "{:g}".format(output_h)
print(output_h)
print(output_i)
