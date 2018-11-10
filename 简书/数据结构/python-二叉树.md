||vector(静态)|list(动态)|tree
|---|---|---|---|
|search|√|X|√|
remove/insert|X|√|√|
- 之所以要引入树，是因为树擅长搜索也擅长插入删除
####1. 遍历概念
>前序遍历：根节点->左子树->右子树
中序遍历：左子树->根节点->右子树
后序遍历：左子树->右子树->根节点
![image.png](https://upload-images.jianshu.io/upload_images/6634703-14b7ee678e27e06f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
前序遍历：abdefgc
中序遍历：debgfac
后序遍历：edgfbca
####2. 二叉树实现
```
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print (root.elem,end=" ")
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print (root.elem,end=" ")
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print (root.elem,end=" ")

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print (node.elem,end=" ")
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild  # 开始查看它的右子树

    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print (node.elem,end=" ")
            node = node.rchild  # 开始查看它的右子树

    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print (myStack2.pop().elem,end=" ")

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print (node.elem,end=" ")
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

if __name__ == "__main__":
    elems = range(15)
    tree =Tree()
    for elem in elems:
        tree.add(elem)

    print('\n递归实现先序遍历:')
    tree.front_digui(tree.root)
    print('\n递归实现中序遍历:')
    tree.middle_digui(tree.root)
    print ('\n递归实现后序遍历:')
    tree.later_digui(tree.root)
    print('\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)
    print('\n堆栈实现中序遍历:')
    tree.middle_stack(tree.root)
    print('\n堆栈实现后序遍历:')
    tree.later_stack(tree.root)
    print ('\n队列实现层次遍历:')
    tree.level_queue(tree.root)
```
```
递归实现先序遍历:
0 1 3 7 8 4 9 10 2 5 11 12 6 13 14 
递归实现中序遍历:
7 3 8 1 9 4 10 0 11 5 12 2 13 6 14 
递归实现后序遍历:
7 8 3 9 10 4 1 11 12 5 13 14 6 2 0 
堆栈实现先序遍历:
0 1 3 7 8 4 9 10 2 5 11 12 6 13 14 
堆栈实现中序遍历:
7 3 8 1 9 4 10 0 11 5 12 2 13 6 14 
堆栈实现后序遍历:
7 8 3 9 10 4 1 11 12 5 13 14 6 2 0 
队列实现层次遍历:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
```
