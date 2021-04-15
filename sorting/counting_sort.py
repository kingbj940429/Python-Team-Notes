'''계수 정렬'''
'''
O(N+K) N은 데이터개수, K는 데이터 최대값
min 값과 max 값의 차이가 1,000,000보다 작을떄 효과적

삽입, 선택, 퀵 정렬과 달리 비교 기반의 정렬 알고리즘은 아니다.
'''

n = 5
data = [8, 5, 4, 7, 2]

''' Counting Sort '''
# Initialize a list whose size is greater than a range of all values.
count = [0] * (max(data) + 1)

for i in range(n):
    count[data[i]] += 1 # Increase the value in the index.

for i in range(len(count)): # Check the sort information recorded on the list.
    for j in range(count[i]):
        print(i) # Print each index as many times as it appears.