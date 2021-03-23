N = int(input())

input_list = [[x for x in input().split()] for y in range(N)]

print(input_list)



#input_list = [list(input()) for _ in range(N)] 문자열 한줄씩 리스트에 담기
#input_list = [list(map(int,input())) for _ in range(N)] 문자열 한줄씩 리스트에 담기


#input_data = [list(input()) for _ in range(N)] ===========> [['A', 'A', 'B'], ['A', 'C', 'D'], ['B', 'D', 'E']]