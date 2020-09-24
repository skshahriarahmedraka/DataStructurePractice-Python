
class Node:
    def __init__(self):
        self.ParentNode=None
        self.NodeData=None
        self.LeftNode=None
        self.RightNode=None
class Binary_Tree:
    def __init__(self):
        self.Root=None
    def Add_Node(self,data):

        extranode=self.Root
        if extranode is None:
                extranode=Node()
                extranode.NodeData=data
                self.Root=extranode
                return 1

        while True:
            
            if data <= extranode.NodeData:
                if extranode.LeftNode is None:
                    extranode.LeftNode=Node()
                    extranode.LeftNode.NodeData=data
                    extranode.LeftNode.ParentNode=extranode
                    print("Left")
                    return 1
                else:
                    extranode=extranode.LeftNode
            elif data > extranode.NodeData:
                if extranode.RightNode is None:
                    extranode.RightNode=Node()
                    extranode.RightNode.NodeData=data
                    extranode.RightNode.ParentNode=extranode
                    print("Right")
                    return 1
                else:
                    extranode=extranode.RightNode


def main():
    b1=Binary_Tree()
    n=int(input("(binary tree) how many data : "))
    for i in range(1,n+1):
        s=input(f"{i}th input : ")
        b1.Add_Node(s)





if __name__=="__main__":
    main()
