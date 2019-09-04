"""
栈：相当于一端开口一端封闭的容器
数据进入栈之后，在栈顶，同时占据了一个栈的位置，当再有新的数据加进来之后，新的数据就是栈顶的位置
之前的数据在栈顶的下一个位置，由于栈是一端开口的，所以只能对栈顶的元素进行操作
"""
# 类的成员函数必须要有self这个参数，并且位于第一位，self代表实例对象自身，可以用self引用类的属性和成员函数
class Stack:
    def __init__(self):
        #定义列表用来作为实现栈的容器
        self.items = []
    def isEmpty(self):
        #空栈返回True，否则返回False
        return len(self.items)==0
    def push(self,item):
        #入栈操作，item为入栈数据
        self.items.append(item)
    def pop(self):
        #出栈操作，返回列表中制定元素并删除，默认返回列表最后一个元素(栈顶)
        if self.items is not []:
            return self.items.pop()
        else:
            return None
    def peek(self):
        #返回栈顶元素，但是不删除
        return self.items[-1]
    def size(self):
        #返回栈的大小
        return len(self.items)

#创建实例：
s = Stack()
print(s.isEmpty())
s.push("Hello World")
s.push("Python Stack")
print("栈顶元素："+s.peek())
s.push("Data Structure")
print("栈顶元素："+s.peek())
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print("栈顶元素："+s.peek())
print(s.size())
