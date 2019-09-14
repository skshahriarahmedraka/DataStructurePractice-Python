class node:
    def __init__(self,data):
        self.visit=True
        self.parentnode=None
        self.nodedata=data
        self.leftnode=None
        self.rightnode=None
class binarytree:
    def __init__(self):
        self.root=None
    def insert(self,data,extranode=None):
        if extranode is None:
            extranode=self.root
        if self.root is None:
            self.root=node(data)
            return self.root
        else:
            if extranode.nodedata>=data:
                if extranode.leftnode is None:
                    extranode.leftnode=node(data)
                    extranode.leftnode.parentnode=extranode
                    return extranode.leftnode
                else:
                    return self.insert(data,extranode=extranode.leftnode)
            else:
                if extranode.rightnode is None:
                    extranode.rightnode=node(data)
                    extranode.rightnode.parentnode=extranode
                    return extranode.rightnode
                else:
                    return self.insert(data,extranode=extranode.rightnode)
    def showbinarytree(self,extranode=None):
        if extranode==None:
            extranode=self.root
            if extranode==None:
                print("binary tree is empty")
    def DFS(self,data):
        extranode=self.root
        while True:
            if extranode.nodedata == data:
                print("data is found")
                self._DFS()
                return extranode
            extranode.visit=False
            if extranode.leftnode is not None and (extranode.leftnode.visit) :
                extranode=extranode.leftnode
                # print("leftnode")
                continue
            elif extranode.rightnode is not None and (extranode.rightnode.visit):
                extranode=extranode.rightnode
                # print("right")
                continue
            else:
                if extranode.parentnode is not None:
                    extranode=extranode.parentnode
                    # print("parent")
                    continue
                else:
                    print("data is not found")
                    self._DFS()
                    return
    def _DFS(self):
        extranode=self.root
        while True:
            
            extranode.visit=True
            if extranode.leftnode is not None and (extranode.leftnode.visit) :
                extranode=extranode.leftnode
                # print("leftnode")
                continue
            elif extranode.rightnode is not None and (extranode.rightnode.visit):
                extranode=extranode.rightnode
                # print("right")
                continue
            else:
                if extranode.parentnode is not None:
                    extranode=extranode.parentnode
                    # print("parent")
                    continue
                else:
                    return

        
    

            
if __name__=="__main__":
    n=int(input("how many imput you want to give : "))
    bt=binarytree()
    for i in range(n):
        bt.insert(input())
    bt.DFS(input("give a number for DFS search : "))
    n=int(input("how many imput you want to give : "))
    bt=binarytree()
    for i in range(n):
        bt.insert(input())
    bt.DFS(input("give a number for DFS search : "))
                    


