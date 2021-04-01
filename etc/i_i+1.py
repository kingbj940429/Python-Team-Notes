'''
zip 이용하여 i+1에 접근하기
'''

def solution(myList):
    result = []

    #list가 짧은것 기준
    for num1,num2 in zip(myList, myList[1:]):
        result.append(abs(num1-num2))
    return result

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(len(mylist), len(mylist[1:]))
    print(solution(mylist))