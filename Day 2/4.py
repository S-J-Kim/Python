s = '파이썬'

print(s.encode())  # 문자열 암호화. "파이썬" 을 암호화 하면 "b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'"

print(b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac'.decode()) # 문자열 복호화