def average(scores):
	sum = 0
	for score in scores:
		sum += score
	avg = sum / len(scores)
	return avg

students =	[
        [80, 97, 87, 90, 95],
	[85, 88, 78, 92, 78],
	[90, 90, 80, 78, 79]
			]

for student in students:
	avg = average(student)
	print("평균: {}".format(avg))
