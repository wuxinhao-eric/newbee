"""
队列：两端都开口的容器，想象一下我们平常排的队伍，一头为队尾，一头为队首
队尾只能进行添加，队首只能进行删除，‘不能插队’
"""
class Quene(object):
    def __init__(self):
        #同样用列表来实现队列
        self.queue = []
    def isEmpty(self):
        return True if self.queue == [] else False
    def enquene(self,item):
        #队尾插入数据item
        self.queue.append(item)
    def dequene(self):
        #队列中存在数据才能删除
        if self.queue is not []:
            return self.queue.pop()
        else:
            return None
    def head(self):
        #返回队首数据
        if self.queue is not []:
            return self.queue[0]
        else:
            return None
    def tail(self):
        if self.queue is not []:
            return self.queue[-1]
        else:
            return None
    def size(self):
        return len(self.queue)

#创建实例：
q = Quene()
print(q.isEmpty())
q.enquene("Hello World")
q.enquene("Hello Python")
print(q.isEmpty())
print("队首元素:"+q.head())
print("队尾元素:"+q.tail())
q.enquene("Python Queue")
print(q.size())
print(q.dequene())
print(q.dequene())