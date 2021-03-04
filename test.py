datas = [1,10,5,8,7,6,4,3,2,9]
data_len = len(datas)

for i in range(data_len):
    for j in range(i,data_len):
        if(datas[i] > datas[j]):
            datas[i], datas[j] = datas[j], datas[i]

print(datas)