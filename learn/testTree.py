"""
树:树是一种非线性的数据结构，具有很好的层次性
二叉树的存储方式分为顺序存储和链式存储，顺序存储采用列表方式，而链式存储采用链表方式
二叉树的链式存储中，树节点包含数据域、左子链域和右子链域
"""

#定义树节点类
class Node(object):
    def __init__(self,data = -1,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
#定义二叉树类,root是Node的对象，表示根节点
class BinaryTree(object):
    def __init__(self):
        self.root = Node()
    def add(self,data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            #以列表存储二叉树，每一次都是空的列表，从根节点开始加数据，这里保证加的原则是先左后右
            queue = []
            queue.append(self.root)
            while queue:
                #将列表第一个元素移除（作为根节点），检查左右子树是否有值
                tree_node = queue.pop(0)
                if tree_node.lchild is None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild is None:
                    tree_node.rchild = node
                    return
                else:
                    #左右子树都有值，则将值加入列表，那么下一个根节点就是原本根节点的左子树了
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)
    #先序遍历
    def pre_order(self,start):
        #其基本思想：根节点-左子树-右子树
        node = start
        if node is None:
            return
        print(node.data,end='')
        if node.lchild is None and node.rchild is None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)
    #中序遍历
    def in_order(self,start):
        # 其基本思想：左子树-根节点-右子树
        node = start
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.data,end='')
        self.in_order(node.rchild)
    #后序遍历
    def post_order(self,start):
        # 其基本思想：左子树-右子树-根节点
        node = start
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.data,end='')
    def isEmpty(self):
        return True if self.root.data == -1 else False
    def length(self):
        return len(self.queue)

#创建实例
if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)

    print('pre order:')
    tree.pre_order(tree.root)
    print('\nin order:')
    tree.in_order(tree.root)
    print('\npost order:')
    tree.post_order(tree.root)
