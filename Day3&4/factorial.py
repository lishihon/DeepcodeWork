def factorial(num):
    '''接收一个参数num，返回代表阶乘的字典'''
    result = {}
    for i in range(num):
        result[i] = i*i
    print(result)


factorial(8)