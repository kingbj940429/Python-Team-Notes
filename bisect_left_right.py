from bisect import bisect_left, bisect_right

a = [1,2,4,4,5]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

def count_by_range(b , left_value, right_value):
    left_index = bisect_left(b, left_value)
    right_index = bisect_right(b, right_value)

    return right_index -  left_index

b = [1,2,3,3,3,3,4,4,8,9]

print("4와 4사이의 갯수는 %d" % count_by_range(b, 4, 4))
print("-1와 3사이의 갯수는 %d" %count_by_range(b, -1 ,3))
