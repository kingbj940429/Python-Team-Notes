''' 파이썬에서만 사용 가능한 퀵정렬'''
''' 기존 퀵정렬보다는 조금 느림 '''

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]#분할된 왼쪽
    right_side = [x for x in tail if x > pivot]#분할된 오른쪽

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))