"""
이것은 주석입니다.
실행 시 출력되지 않습니다.
"""

print("몬스터 리그에 오신 것을 환영합니다.")
print("[1] 화끈몬\t [2] 축축몬\t[3] 수풀몬\n")
selected_num = input('플레이할 "몬스터"의 번호를 선택해주세요.:')
# 사용자의 숫자를 입력받습니다.

user_name = input("당신의 이름을 입력해 주세요.:") # 게임 플레이어의 이름을 입력합니다.
print(selected_num+"번을 선택하셨습니다."+user_name+" 님 환영합니다.")
print("{}번을 선택하셨습니다. {}님 환영합니다.".format(selected_num,user_name))
rint("{0}번을 선택하셨습니다. {1}님 환영합니다.".format(selected_num,user_name))
rint("{1}번을 선택하셨습니다. {0}님 환영합니다.".format(selected_num,user_name))
rint("{selected_num}번을 선택하셨습니다. {user_name}님 환영합니다.".format(selected_num=100,user_name="마스터"))
rint(f"{selected_num}번을 선택하셨습니다. {user_name}님 환영합니다.")

monster = ['화끈몬', '축축몬', '수풀몬']
print(monster[0])
print(monster[1])
print(monster[2])
# type() -> list 자료형 출력
print(type(monster))
print(len(monster))
# len() 이용하기
# indexerror -> list에서 조심

monsters = []
monsters.append('물물몬')
monsters = monster + ['불몬','바위몬']
print(monsters)

monsters.insert(1, '찌릿몬')
print(monsters)
new_monsters = ['가스몬','바람몬']
monsters.extend(new_monsters)
print(monsters)

# 리스트의 삭제

monsters.remove('가스몬')
monsters.pop(3)
monsters.pop()
del monsters[0]
