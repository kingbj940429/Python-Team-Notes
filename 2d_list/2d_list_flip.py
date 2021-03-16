''' 2차원 배열 뒤집기 '''

def file_2d_list(data_list, N):
    fliped_list = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            fliped_list[i][j] = data_list[j][i]
    return fliped_list

N = 3
data_list = [list(input()) for _ in range(N)]

result_list = file_2d_list(data_list, N)
print(result_list)
            