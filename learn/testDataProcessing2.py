import numpy as np
import pandas as pd
'''
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df)
df.columns = ['yi','er','san']
print(df)

phone = pd.Series([21000,12000,18000],index=['111','2222','3333'])
print(phone)
print(phone[:2])
# loc是基于行标签 iloc是基于行号
print(df.iloc[1])
# 通过两种方式获得列，可以在后加条件
df.yi
df[df['yi'] == 1]
df['这是新增的'] = True
print(df)
df = df.drop('这是新增的',axis=1)
print(df)
'''
'''
df.index = ['yiyi','erer','sansan']
print(df)
print(df.iloc[1])
print(df.loc['yiyi'])
'''
'''
print(df.iloc[2].yi)
# df.iloc[2] = ['lalala','qaq','eee']
# df.iloc[2] = {'yi':'sss','er':'s','san':'s'} 不可以
# df.iloc[3] = ['111','222','333'] 不可以在使用这种方法,下标越界
# 加一行数据
df = df.append(pd.DataFrame([{'yi':'sss','er':'s','san':'s'}]),ignore_index=True,sort=True)
# df.drop(2,inplace=True)
print(df)

df['id'] = range(101,105)
df.set_index('id',inplace=True)
print(df)
print(df.isnull().sum())
print(df['yi'].isnull().values.any())
# 删除有nan的行
df.dropna()
df.dropna(how='all')
# 超过两个缺失值的行
df.dropna(thresh=2)
# 根据年龄分配平均值
df['age'].fillna(df.groupby('gender')['age'].transform('mean'),inplace=True)
# 有规律数据的填充
df.interpolate()
# 将第一列作为索引df = pd.read_csv(index_col=0)
'''
# 这个方法中还有个na_values可以指定none值
income = pd.read_excel(r'D:\\icbc_file\\train1.xls')
pd.set_option('display.max_columns',None)
print(income.head())
income.loc[income['demog_inc'] == 0,'demog_inc'] = np.nan
print(income.head())
income.tail()
income.info()
income.dtypes
income.describe()
income.isnull().any()
income.isnull().sum()
income.count()

