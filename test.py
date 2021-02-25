def garo_count(input_list):
    total_cnt = 0
    for i  in range(N):
        d1_list = str(input_list[i])
        cnt = 0
        for j in range(N):
            if(input_list[i][j] == '.'):
                cnt = cnt + 1
                if(cnt >= 2):
                    total_cnt = total_cnt + 1
                    break
            else : 
                cnt = 0
    return total_cnt

def sero_count():
    return False

N = int(input())
if __name__ == "__main__":

    input_list = [list(input()) for _ in range(N)]
    garo_cnt = garo_count(input_list)
    print(garo_cnt)

