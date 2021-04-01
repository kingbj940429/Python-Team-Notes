#n제곱
import math

num = int(input())

result = math.pow(num, 2)#두번째 인장에 n제곱할 수를 넣어준다.
print(round(result))


#(num ** 2) 이런식도 가능하다. => 이건 math를 import 시키지 않아도 되서 더 나은듯 


'''
되게 좋은 예제인것 같다.

num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    print(idx, number)
    answer += int(number) * (base ** idx)

'''