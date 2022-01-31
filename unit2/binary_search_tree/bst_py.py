import math
class node:
    def __init__(self,key=math.inf):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
class BST:
    def __init__(self,ls=[]):
        self.root = node()
        self.build_bst(ls)
    def isEmpty(self):
        if(self.root.key==math.inf):
            return True
        return False
    def inorder(self,Node):
        if(Node==None):
            return
        self.inorder(Node.left)
        print(Node.key,end=" ")
        self.inorder(Node.right)
    def insert(self,val):
        try:
            if(self.isEmpty()):
                self.root.key = val
            else:
                temp = self.root
                loop = True
                while(loop):
                    if(val<temp.key and temp.left!=None):
                        temp = temp.left
                    elif val<temp.key:
                        temp.left = node(val)
                        temp.left.parent = temp
                        # print("Successfully Inserted.")
                        loop = False
                    elif val>temp.key and temp.right!=None:
                        temp = temp.right
                    elif val>temp.key :
                        temp.right = node(val)
                        temp.right.parent = temp
                        # print("Successfully Inserted.")
                        loop = False
                    else:
                        print("Value is already in the BST.")
        except:
            print("You Entered a Wrong Value which can't be compared.")
    def build_bst(self,ls):
        for i in ls:
            self.insert(i)
    def min_element_in_subtree(self,Node):
        temp = Node
        while(temp.left != None):
            temp = temp.left 
        return temp.key
    def next_larger(self,Node):
        if(Node.right==None):
            return Node.parent.key
        return self.min_element_in_subtree(Node.right)
    def search_node_by_val(self,val):
        temp = self.root
        while(True):
            if(temp.key == val):
                # print("Value Found Successfully.")
                return temp
            elif(temp.key>val and temp.left!=None):
                temp = temp.left 
            elif(temp.key<val and temp.right!=None):
                temp = temp.right
            else:
                # print("No Such Value is there in BST.")
                return None
    def deletion(self,Node):
        if(Node.left==None and Node.right==None):
            if(Node.parent.key>Node.key):
                Node.parent.left = None
            else:
                Node.parent.right = None
        else:
            to_replace_with = self.next_larger(Node)
            replacing_node = self.search_node_by_val(to_replace_with)
            if(replacing_node.parent.key>replacing_node.key):
                replacing_node.parent.left = None
            else:
                replacing_node.parent.right = None
            Node.key = to_replace_with
    def height(self,Node):
        if(Node == None):
            return -1
        return max(self.height(Node.left),self.height(Node.right)) + 1
if __name__=='__main__':
    tree = BST()
    tree.insert(20)
    tree.insert(15)
    tree.insert(30)
    tree.insert(27)
    tree.insert(39)
    tree.insert(1)
    tree.inorder(tree.root)
    print()
    print(tree.min_element_in_subtree(tree.root))
    print(tree.next_larger(tree.root))
    smallest = tree.search_node_by_val(1)
    print(tree.next_larger(smallest))
    tree.deletion(tree.search_node_by_val(20))
    tree.inorder(tree.root)
    print(tree.height(tree.search_node_by_val(30)))