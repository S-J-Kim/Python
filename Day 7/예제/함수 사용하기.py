def print_string(text, count=2):
    for i in range(count):
        print(text)

print_string("안녕하세요", 3)


# 가변 매개변수. 매개변수의 갯수를 특정할 수 없을 때 사용. 매개변수는 튜플의 형태로 전달 됨
def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s
        
    return result

print(merge_string("아버지", "가방에", "들어가신다"))

# 딕셔너리 형태의 가변 매개변수
def print_team(**players):
    for k in players.keys():
        print(f'{k} = {players[k]}')
    
print_team(이천웅='중견수', 김용의='1루수')
