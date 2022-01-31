from youtube_dl import main
import bst_py
import math
class node:
    def __init__(self,key=math.inf):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
class avl(bst_py.BST):
    def __init__(self,ls=[]):
        self.root = node()
        self.build_bst(ls)
    def rotation_identifier(self,Node :node)-> int:
        if(self.bf_cal(Node)>1 and self.bf_cal(Node.left)==1):
            return 3
        elif(self.bf_cal(Node)>1):
            return 4
        elif(self.bf_cal(Node)<1 and self.bf_cal(Node.right)==-1):
            return 1
        else:
            return 2
    def rotate_right(self,Node : node) -> None:
        if(Node.parent==None):
            self.root = Node.right
            self.root.parent = None
            Node.left = self.root.right
            if Node.left!=None:
                Node.left.parent = Node
            self.root.right = Node
            Node.parent = self.root
            return
        elif(Node.parent.key<Node.key):
            Node.parent.right = Node.left
        else:
            Node.parent.left = Node.left
        Node.left.parent = Node.parent
        Node.parent = Node.left
        Node.left = Node.parent.right
        if Node.left!=None:
            Node.left.parent = Node
        Node.parent.right = Node
        print("65 height",self.search_node_by_val(65).height)
    def rotate_left(self,Node: node)->None:
        if(Node.parent==None):
            self.root = Node.right
            self.root.parent = None
            Node.right = self.root.left
            if Node.right!=None:
                Node.right.parent = Node  
            self.root.left = Node
            Node.parent = self.root
            return
        elif(Node.parent.key<Node.key):
            Node.parent.right = Node.right
        else:
            Node.parent.left = Node.right
        Node.right.parent = Node.parent
        Node.parent = Node.right 
        Node.right = Node.parent.left 
        if Node.right != None:
            Node.right.parent = Node
        Node.parent.left = Node
    def bf_cal(self,Node: node)->None:
        l = -1 if(Node.left==None) else Node.left.height
        r = -1 if(Node.right==None) else Node.right.height
        return l-r
    def height_new(self,Node: node)->int:
        return max(0 if Node.left==None else Node.left.height+1,0 if Node.right==None else Node.right.height+1)
    def rebalance(self,Node: node)->None:
        Node = Node.parent
        while(Node!=None):
            Node.height = max(self.height(Node.left), self.height(Node.right)) + 1
            bf_node = self.bf_cal(Node)
            if abs(bf_node) > 1:
                rotation = self.rotation_identifier(Node)
                if(rotation==1):
                    #RR
                    self.rotate_left(Node)
                elif(rotation==2):
                    #RL
                    self.rotate_right(Node.right)
                    Node.right.height = self.height_new(Node.right)
                    self.rotate_left(Node)
                elif(rotation==3):
                    #LL
                    self.rotate_right(Node)
                elif(rotation==4):
                    #LR
                    self.rotate_left(Node.left)
                    Node.left.height = self.height_new(Node.left)
                    print(Node.left.height)
                    self.rotate_right(Node)
            Node.height = self.height_new(Node)
            Node = Node.parent
        
    def insert(self,val):
        super().insert(val)
        Node = self.search_node_by_val(val)
        self.rebalance(Node)
if __name__=='__main__':
    tree = avl()
    tree.insert(13)
    print("inorder :",tree.inorder(tree.root))
    tree.insert(5)
    print("inorder :",tree.inorder(tree.root))
    tree.insert(25)
    print("inorder :",tree.inorder(tree.root))
    tree.insert(20)
    print("inorder :",tree.inorder(tree.root))
    tree.insert(16)
    print("inorder :",tree.inorder(tree.root))