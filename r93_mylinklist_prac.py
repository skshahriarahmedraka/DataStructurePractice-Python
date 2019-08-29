class node:
    def __init__(self,data):
        self.previousnode=None
        self.nodedata=data
        self.nextnode=None

class linklist:
    def __init__(self):
        self.root=None
        self.last=None
    def insertstart(self,data):
        newnode=node(data)
        self.root.previousnode=newnode
        newnode.nextnode=self.root
        self.root=newnode
    def insertlast(self,data):
        newnode=node(data)
        if self.root is None:
            self.root=newnode
            self.last=newnode
        else:
            newnode.previousnode=self.last
            self.last.nextnode=newnode
            self.last=newnode
    def search(self,data):
        t=self.root
        while t:
            if data==t.nodedata:
                print(f"found {data} in the linklist")
                return
            t=t.nextnode
        print(f"the {data} is not found in the linklist")
        return
    def delete(self,index):
        t=self.root
        i=0
        while i<index-1:
            tp=t
            t=t.nextnode
        tp.nextnode=t.nextnode
        t.nextnode.previousnode=tp

    def printlist(self):
        t=self.root
        print("linklist printing:")
        while t:
            print(t.nodedata)
            t=t.nextnode
    
    

def main():
    n=int(input("how many you wants to give(last):"))
    li=linklist()
    for i in range(n):
        li.insertlast(input())
    li.printlist()
    '''
    n=int(input("how many you wants to give(first):"))
    for i in range(n):
        li.insertstart(input())
    li.printlist()
    li.search(input("search in the linklist : "))
    '''
    li.delete(int(input("give index to delete : ")))

if __name__=="__main__":
    main()