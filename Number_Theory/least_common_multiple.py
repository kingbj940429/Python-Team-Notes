''' 최소 공배수 '''

'''
두 값은 곱한 값의 최대공약수를 나주면 됨
'''

from math import gcd

def lcm(x, y):
    return x*y // gcd(x,y)

print(lcm(6,8))


''' N개의 최소공배수 '''

def lcms(arr):
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


print(lcms([2, 6, 8, 14]))
