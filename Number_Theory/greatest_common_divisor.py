''' 최대 공약수 '''

'''
유클리드 호제법 공식 이용
ex)
18 24
18를 24로 나눈 나머지 => 6
24를 6로 나눈 나머지 => 0
6은 0으로 나눠짐 => 최대공약수 6
'''

import math#from math import gcd
#직접 구현해야 할때
def gcd_custom(x, y):
    while y:
        x, y = y, x%y
    return x

print(gcd_custom(18, 24))

#math 모듈 사용할때
print(math.gcd(18, 24))