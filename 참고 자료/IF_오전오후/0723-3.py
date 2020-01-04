# 혈압수치와 혈당수치를 입력받아 의심되는 질환을 출력하는 프로그램

bp = int(input("혈압수치: "))
bs = int(input("혈당수치: "))

if bp < 90 or 140 < bp or 120 < bs:
	print("의심되는 질환:")
	if bp < 90:
		print("저혈압")
	elif 140 < bp:
		print("고혈압")
	if 120 < bs:
		print("당뇨병")
else:
	print("의심되는 질환이 없습니다.")
