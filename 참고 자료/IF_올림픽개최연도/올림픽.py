years = list(range(1896, 2030))

for y in years:
	if y % 4 == 0:
		years[y - 1896] = "***"
print(years)
print()

print('1916년은 1차대전으로, 1940년과 1944년은 2차대전으로 취소')

