#문자열이 어떻게 구성되어있는지 확인하는법

#isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어있는지 확인
#isalpha() : 문자열이 알파벳으로만 구성되어있는지 확인
#isidentifier() : 문자열이 식별자로 사용할 수 있는 것인지 확인
#isdecimal() : 문자열이 정수 형태인지 확인
#isdigit() : 문자열이 숫자로 인식될 수 있는 것인지 확인
#isspace() : 문자열이 공백으로만 구성되어 있는지 확인
#islower() : 문자열이 소문자로만 구성되어 있는지 확인
#isupper() : 문자열이 대문자로만 구성되어 있는지 확인

#출력은 True or False
#boolean값으로 나옴

print("TrainA10".isalnum())

print("10".isdigit())

print("abcdede".islower())
