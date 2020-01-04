import datetime

now = datetime.datetime.now()

ap = "오전" if now.hour < 12 else "오후" # 현재시각이 오전인지 오후인지 판단
h = now.hour % 12 # 24시간제를 12시간제로 변환
m = now.minute

print(f'{ap} {h}시 {m}분')