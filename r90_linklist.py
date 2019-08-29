'''import copy
class node:
    def __init__(self,data):
        self.data=data
        print(self.data)
        
    

class linklist:
    def __init__(self):
        self.nextnode=None
    def insert(self,data):
        if self.nextnode==None:
            newnode=node(data)
            self.nextnode=newnode

        else:
            self.insert(data)
    def show(self):
        actualnode=self.nextnode
        print("datas: ")
        
        while actualnode is not  None:
            print(actualnode.data)
            actualnode=actualnode.nextnode
        return 0


def main():
    print("how many input : ")
    n=int(input())
    print("give input :")
    root=linklist()
    x=root
    for i in range(n):
        a=int(input())
        x.insert(a)
    root.show()
        
if __name__=="__main__":
    main()'''

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
class SLinkedList:
    def __init__(self):
        self.headval = None
    
    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
    
    # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
    
list.headval.nextval = e2
e2.nextval = e3
    
list.AtBegining("Sun")
    
list.listprint()
'''
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3'''