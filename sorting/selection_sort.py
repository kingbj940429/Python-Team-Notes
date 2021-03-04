''' 가장 일반 적인 정렬 O(N^2) 버블정렬과 비슷하다고 보면 됨'''

n = 5
data = [8, 5, 4, 7, 2]

''' Selection Sort '''
for i in range(n):
    min_index = i # The index of the minimum value.
    for j in range(i + 1, n):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i] # Swap.

for x in data:
    print(x)