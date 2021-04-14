'''삽입정렬 : 데이터가 거의 정렬되어있을 때 효과적이다.'''

'''
1) 삽입정렬의 핵심은 "이미 정렬된"이다. 따라서 삽입할 데이터의 값보다 작으면 거기다 그냥 삽입하면된다.
2) 무조건 두번째 값부터 시작한다. 첫번째 값은 이미 정렬되었다고 가정하기 때문이다.
3) 시간복잡도 O(N^2) 를 가지지만, 거의 정렬되어있으면 O(N) 를 가지기도 함.
'''

n = 5
data = [8, 5, 4, 7, 2]

''' Insertion Sort '''
for i in range(1, n):
    for j in range(i, 0, -1): # The variable j decreases from i to 1.
        if data[j - 1] > data[j]: # Move left. 
            data[j - 1], data[j] = data[j], data[j - 1] # Swap.
        else: # When reaching a smaller value, then stop.
            break

for x in data:
    print(x)