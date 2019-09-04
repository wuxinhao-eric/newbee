from collections import Counter
from math import log
import numpy as np

# X:数据集 y:结果集 d:选定的维度 value:选定的阈值
def spilt(X, y, d ,value):
    index_a = (X[:,d] <= value)
    index_b = (X[:,d] > value)
    return X[index_a],X[index_b],y[index_a],y[index_b]

# 计算熵的函数，只需要传入结果集即可，不同结果所占比例引起熵的变化
def entropy(y):
    counter = Counter(y)
    # 熵
    res = 0.0
    for num in counter.values():
        p = num / len(y)
        res += -p * log(p)
    return res

def try_split(X,y):
    best_entropy = float('inf')
    best_d , best_v = -1,-1
    # 遍历X的维度
    for d in range (X.shape[1]):
        sorted_index = np.argsort(X[:,d])
        for i in range (1,len(X)):
            if X[sorted_index[i-1]] != X[sorted_index[i],d]:
                v = (X[sorted_index[i-1],d] + X[sorted_index[i],d])/2
                x_l,x_r,y_l,y_r = spilt(X,y,d,v)
                e = entropy(y_l)+entropy(y_r)
                if e < best_entropy:
                    best_entropy,best_d,best_v = e,d,v
    return best_entropy , best_d , best_v

