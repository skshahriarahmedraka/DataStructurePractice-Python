# @Author: sk shahriar ahmed raka 
# @Date: 2020-10-19 15:28:39 
# @Mail: skshahriarahmedraka@gmail.com 


class Node:
    def __init__(self , M_way):
        print("$$$ New Node Created $$$")
        self.ParentNode =None
        self.NodeValues =[]
        self.ChildLinks =[None ] *M_way


class MTree:
    def __init__(self ,M_way):
        self.Root =Node(M_way)
        self.M_way =M_way
    def Add_Node(self ,data):
        extranode =self.Root
        if len(extranode.NodeValues) < self.M_way - 1:
            extranode.NodeValues.append(data)
            extranode.NodeValues.sort()
            self.Root = extranode
            print("Root Node")
            print(extranode.NodeValues)
            return 1
        
        i=0
        while i < self.M_way - 1:
            
            if len(extranode.NodeValues) < self.M_way - 1:
                
                extranode.NodeValues.append(data)
                extranode.NodeValues.sort()
                
                print(f"current Node Values {extranode.NodeValues}\n")
                return 1

            if data < extranode.NodeValues[i]:
                if extranode.ChildLinks[i] is None:
                    extranode.ChildLinks[i] = Node(self.M_way)
                    extranode.ChildLinks[i].NodeValues.append(data)
                    extranode.ChildLinks[i].NodeValues.sort()
                    
                    print(f"current Node Values {extranode.ChildLinks[i].NodeValues}\n")
                    return 1
                else:
                    extranode = extranode.ChildLinks[i]
                    i=0
                    continue

            elif data > extranode.NodeValues[i] and i == (self.M_way - 2):
                if extranode.ChildLinks[i] is None:
                    extranode.ChildLinks[i] = Node(self.M_way)
                    extranode.ChildLinks[i].NodeValues.append(data)
                    extranode.ChildLinks[i].NodeValues.sort()
                    
                    print(f"current Node Values {extranode.ChildLinks[i].NodeValues}\n")
                    return 1
                else:
                    extranode = extranode.ChildLinks[i]
                    i=0
                    continue
            i+=1



def main():
    n = int(input("M-way search tree \nValue of M : "))
    t1 = MTree(n)
    n = int(input("amount of  data you want to put : "))
    for i in range(n):
        t1.Add_Node(int(input(f"{i + 1}th : ")))


if __name__ == "__main__":
    main()
    