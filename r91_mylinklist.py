"linklist reversely print, reversely pushed"
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=node(data)
        newnode.next=self.root
        self.root=newnode
    def printlist(self):
        temp=self.root
        while(temp):
            print(temp.data)
            temp=temp.next



def main():
    list=linklist()
    n=int(input("how many data you want to give as input :"))
    for i in range(n):
        list.insert(input())
    print("your given input are :")
    list.printlist()
    


if __name__=="__main__":
    main()