"""
print("这是python")

print("deep learning")

#列表：有序存储数据，相当于数组

testlist = ['c++','java','python']
print(testlist)

#遍历列表元素
for i in range(len(testlist)):
    print(testlist[i])

for index,value in enumerate(testlist):
    print(index,value)

#数值自增长的列表，第一个参数是开始，第二个参数是结束
list1 = range(10)
list2 = range(11,20)

for i in range(len(list1)):
    print(list1[i])
for i in range(len(list2)):
    print(list2[i])


#二维列表
testlist = [["cpu","内存"],["硬盘","声卡"]]
for i in range(len(testlist)):
    print(testlist[i])

for i in range(len(testlist)):
    list1 = testlist[i];
    for j in range(len(list1)):
        print(list1[j])

#列表中的元素是相同的数据类型，元组中的元素可以是不同的数据类型，一旦定义不能修改
t = (1,"Python",'A','Java')
print(t)
#unicode字符串，通常用于处理中文
var = u"我要学习。"
print(var)


#字典，有一个key一个value
d = {'name':'小明','sex':'男','age':'18'}
#遍历字典元素
for key in d.keys():
    print('键为:'+key+'值为:'+d[key])
#集合：无序排列的元素组成,可变集合set，不可变集合frozenset->创建后不能修改
s = set('python')
print(s)
"""
"""
var  = 3.1468456
print(round(var,5))
#返回5/2的商和余数
print(divmod(5,2))
"""

str1 = "hello world Python"
#以参数为分隔符，返回一个列表
list1 = str1.split(" ")
print(list1)
str2 = "hello world\nPython"
print(str2)
#以行分隔符为依据分割返回一个列表
list2 = str2.splitlines()
print(list2)

p = [2]
print(p)
