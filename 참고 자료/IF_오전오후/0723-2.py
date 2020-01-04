def findbirthday(ssn):
	if ssn[7] in ['1', '2', '5', '6']:
		year = 1900 + int(ssn[0:2])
	elif ssn[7] in ['3', '4', '7', '8']:
		year = 2000 + int(ssn[0:2])
	month = int(ssn[2:4])
	day = int(ssn[4:6])
	return [year, month, day]

ssn = input("주민등록번호: ")
birthday = findbirthday(ssn)
year = birthday[0]
month = birthday[1]
day = birthday[2]
print("생년월일: {}년 {}월 {}일".format(year, month, day))
print("생년월일: {}-{:02}-{:02}".format(year, month, day))