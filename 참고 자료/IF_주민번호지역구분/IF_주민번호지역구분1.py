#registrationi number=rn, local number=ln
rn = int(input("주민등록번호를 (-) 빼고 입력하세요 : "))
ln = rn - (int(rn/1000000) * 1000000)
ln = int(ln/10000)

if 0 <=ln<= 8:
    print("서울")
elif 9<=ln<=12:
    print("부산")
elif 13<=ln<=15:
    print("인천")
elif 16<=ln<=25:
    print("경기")
elif 26<=ln<=34:
    print("강원")
elif 35<=ln<=47:
    print("충청")
elif 48<=ln<=66:
    print("전라")
elif 67<=ln<=91:
    print("경상")
elif 92<=ln<=95:
    print("제주")
else:
    print("잘못된 주민번호입니다.") 
