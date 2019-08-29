
class node:
    def __init__(self,data):
        #self.previous=None
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.root=None
        self.previousnode=None
        
    def insert(self,data):
        newnode=node(data)
        if self.root is None:
            self.root=newnode
            self.previousnode=newnode
        else :
            self.previousnode.next=newnode
            self.previousnode=newnode

    def printlist(self):
        print("data are : ")
        temp=self.root
        while temp:
            print(temp.data)
            temp=temp.next


li=linklist()
n=int(input("how many you want:"))
for j in range(n):
    li.insert(input())
li.printlist()


        
