import pandas as pd
import numpy as np
# 数据读入
income = pd.read_excel(r'D:\\icbc_file\\train1.xls')
# 重复观测的检测
print('数据集中是否存在重复观测：\n',any(income.duplicated()))
income.drop_duplicates(inplace=True)
print(income.shape)
# 缺失值处理
print('数据集中是否存在缺失值：\n',any(income.isnull()))
# 查看存在缺失值的属性
income.apply(lambda x:np.sum(x.isnull()))
'''
删除法1：删除缺省记录
income.dropna()
删除法2：删除相应变量
income.drop('xxx',axis=1)
'''
# 前向填充：income.fillna(method='ffill')
# 后向填充：income.fillna(method='bfill')
# 常数填充：income.fillna(value=0)
# 分别用众数填充（mean均值 median中位数）
income.fillna(value = {'demog_age':income.demog_age.mode()[0],
                       'rfm3':income.rfm3.mode()[0]},inplace=True)
# 检测是否存在异常值
xbar = income.demog_age.mean()
xstd = income.demog_age.std()
# 异常值检测标准差法
print('标准差法异常值上限检测：\n',any(income.demog_age > xbar + 2 * xstd))
print('标准差法异常值下限检测：\n',any(income.demog_age < xbar - 2 * xstd))
# 异常值检测箱线图法
Q1 = income.demog_age.quantile(q = 0.25)
Q3 = income.demog_age.quantile(q = 0.75)
IQR = Q3 - Q1
print('箱线图法异常值上限检测：\n',any(income.demog_age > Q3 + 1.5 * IQR))
print('箱线图法异常值下限检测：\n',any(income.demog_age < Q1 - 1.5 * IQR))
'''
import matplotlib.pyplot as plt
# 设置绘图风格
plt.style.use('ggplot')
# 绘制直方图
income.demog_age.plot(kind='hist',bins = 30,density=True)
# 绘制核密度图
income.demog_age.plot(kind='kde')
plt.show()

'''
'''
outlier_step = 1.5 * IQR
for i in range(income.shape[0]):
    if income.demog_age[i] < Q1 - outlier_step:
        income.drop(index=i,inplace=True)
'''
print(income.shape)
print('异常值替换之前的数据统计特征：\n',income.demog_age.describe())
UL = Q1 - 1.5 * IQR
print(UL)
# 找出高于判别下限的最小值
replace_value = income.demog_age[income.demog_age > UL].min()
print(replace_value)
# 替换低于判别下限的异常值
income.demog_age[income.demog_age < UL] = replace_value
print('异常值替换后的数据统计特征：\n',income.demog_age.describe())


