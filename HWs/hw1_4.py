class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
    def SetChild(self, lchild, rchild):
        self.lchild = lchild
        self.rchild = rchild
    

class Tree:
    def __init__(self, root):
        self.root = root
        
    def Visit(self, node):
        print(node.data)

    def GetRootNode(self):
        return self.root

    def InorderTraverse(self, node):
        if node:
            self.InorderTraverse(node.lchild)
            self.Visit(node)
            self.InorderTraverse(node.rchild)

    def PreorderTraverse(self, node):
        if node:
            self.Visit(node)
            self.PreorderTraverse(node.lchild)
            self.PreorderTraverse(node.rchild)

    def PostorderTraverse(self, node):
        if node:
            self.PostorderTraverse(node.lchild)
            self.PostorderTraverse(node.rchild)
            self.Visit(node)

Node1 = Node(15)
Node2 = Node(1)
Node3 = Node(37)
Node4 = Node(61)
Node5 = Node(26)
Node6 = Node(59)
Node7 = Node(48)

Node1.SetChild(Node2, Node3)
Node2.SetChild(Node4, Node5)
Node3.SetChild(Node6, Node7)

Tree1 = Tree(Node1)

print("Prerder Traversal")
Tree1.PreorderTraverse(Node1)
print("Inorder Traversal")
Tree1.InorderTraverse(Node1)
print("Postorder Traversal")
Tree1.PostorderTraverse(Node1)
