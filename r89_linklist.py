class node:
    def __init__(self,data):
        self.data=data
        self.nextnode=None

    def remove(self,data,previousnode):
        if self.data==data:
            previousnode=self.nextnode
            del self.data
            del self.nextnode
        else:
            if self.nextnode is not None:
                remove(data,self)


class linkedlist(object):
    def __init(self):
        self.head=None
        self.counter=0
    def traverselist(self):
        actualnode=self.head
        while actualnode is not None:
            print(f" {actualnode.data}")
            actualnode=actualnode.nextnode


    def insertstart(self,data):
        self.counter+=1
        newnode=node(data)
        if not self.head:
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode
    def size(self):
        return self.counter

    def insertend(self,data):
        if self.head is None:
            self.insertstart(data)
            return
        self.counter+=1
        newnode=node(data)
        actualnode=self.head
        while actualnode is not None:
            actualnode=actualnode.nextnode
        actualnode.nextnode=newnode

    def remove(self,data):
        self.counter-=1
        if self.head:
            if data== self.head.data:
                self.head=self.head.nextnode
            else:
                 self.head.remove(data,self.head)


li=linkedlist()
li.insertend(12)
li.insertend(13)
li.insertend(188)
li.insertend(199)