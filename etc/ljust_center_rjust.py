'''
n 만큼 공백을 만들 수 있다.
'''

s = '가나다라'
n = 7

print(s.ljust(n)) # 좌측 정렬
print(s.center(n)) # 가운데 정렬
print(s.rjust(n)) # 우측 정렬