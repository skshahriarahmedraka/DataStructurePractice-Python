class node:
    def __init__(self,data):
        self.nodedata=data
        self.leftnode=None
        self.rightnode=None
        self.parent=None

class binarytree:
    def __init__(self):
        self.root=None
    def insert(self,data,extranode=None):
        if extranode==None:
            extranode=self.root
        if self.root==None:
            self.root = node(data)
        else :
            if data<=extranode.nodedata:
                if extranode.leftnode is None:
                    extranode.leftnode=node(data)
                    extranode.leftnode.parent=extranode
                    print("left")
                    return
                else:
                    return self.insert(data,extranode=extranode.leftnode)
            else:
                if extranode.rightnode is None:
                    extranode.rightnode=node(data)
                    extranode.rightnode.parent=extranode
                    print("right")
                    return
                else:
                    return self.insert(data,extranode=extranode.rightnode)
         
    def search(self,data,extranode=None):
        if extranode is None:
            extranode=self.root
        if self.root.nodedata ==data :
            print("data is present in the binary tree")
            return self.root
        
        else:
            if extranode.nodedata==data:
                print("data is present in the binary tree")
                return extranode
            elif extranode.nodedata>data and extranode.leftnode is not None:
                print("left")
                return self.search(data,extranode=extranode.leftnode)
            elif extranode.nodedata<data and extranode.rightnode is not None:
                print("right")
                return self.search(data,extranode=extranode.rightnode)
            else:
                print("data is not present in the binary tree")
                return None
    def find_minimum(self,extranode=None):
        if extranode is None:
            extranode=self.root
            if extranode is None:
                print("tree is empty")

        if extranode.leftnode is None:
            return extranode.nodedata
        else:
            return self.find_minimum(extranode=extranode.leftnode)
        
    def tree_data(self,extranode=None):
        if extranode is None:
            extranode=self.root
        stack=[]
        while stack or extranode:
            if extranode is not None:
                stack.append(extranode)
                extranode=extranode.leftnode
            else:
                extranode=stack.pop()
                yield extranode.nodedata
                extranode=extranode.rightnode







n=int(input("how many data do you want to give : "))
b=binarytree()
for i in range(n):
    b.insert(input())
z=b.search(input("find a data : "))
print(f"and your data is {z.nodedata}")
print("minimum number in binary tree:")
x=b.find_minimum()
print(x)
print("all the data are : ")
#y=[]
y=list(b.tree_data())
print(y)
