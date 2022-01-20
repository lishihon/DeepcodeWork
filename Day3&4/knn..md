```python
import random
import csv
from unittest import result  #用于读取或写入csv文件

#数据读取
with open('Prostate_Cancer.csv','r') as file:
    reader = csv.DictReader(file)   #该方法用于以字典的形式读取文件
    datas=[row for row in reader]   #将字典导为list

#分组 分训练组和结果组
#为避免数据巧合，所以分组前先打乱数据
random.shuffle(datas)   #该方法专门用来打乱顺序

n=len(datas)//3   #要整数

test_set=datas[0:n]
train_set=datas[n:]   #因为数据较小，所以为3：1，一般为10：1

#knn   影响准确度的一般是K的取值以及距离
#算距离,欧式距离，即每个维度的差的平方之和再开方
def distance(d1,d2):
    res=0  #用来算平方和
    for key in ('radius','texture','perimeter','area','smoothness','compactness','symmetry','fractal_dimension'):
        res+=(float(d1[key])-float(d2[key]))**2    #读取过来后key中的数据是字符串类型，要转为float

    return res**0.5

k=5   #要寻找准确率最大的K
def knn(data):
    #1.距离
    res=[
        {"result":train['diagnosis_result'],"distance":distance(data,train)}
        for train in train_set
    ]

    #2.排序——顺序
    res=sorted(res,key=lambda item:item['distance'])

    #3.取前K个
    res2=res[0:k]

    #4.加权平均    即距离与总距离的比例
    result={'B':0,'M':0}

    #总距离
    sum=0
    for r in res2:
        sum+=r['distance']

    for r in res2:
        result[r['result']]+=1-r['distance']/sum     

    # print(result)
    # print(data['diagnosis_result'])
    if result['B']>result['M']:
        return 'B'
    else:
        return 'M'


# knn(test_set[0])
#测试阶段   计算正确了多少个，然后算准确率
correct=0
for test in test_set:
    result=test['diagnosis_result']
    result2=knn(test)

    if result==result2:
        correct+=1

print(correct)
print(len(test_set))
print("准确率：{:.2f}%".format(100*correct/len(test_set)))
```

