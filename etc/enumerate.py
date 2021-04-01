
arr = ['A', 'B', 'C']

for entry in enumerate(arr):
    print(entry)

for index, val in enumerate(arr):
    print(index, val)

print('==============')

#뒤에 시작 숫자도 조작할수 있다.
for index, val in enumerate(arr, start=1):
    print(index, val)

