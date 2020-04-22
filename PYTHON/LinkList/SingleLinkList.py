#Node Class
class Node:

    #initilazing the Node Objects
    def __init__(self,data=""):
        self.data=data
        self.next=None


class LinkList:
    
    def __init__(self):
        self.head=None

    
    def printLinkList(self):
        temp=self.head
        while(temp):
            print("-->",temp.data,end=" ")
            temp=temp.next


    def insertInBegnning(self,node):
        if self.head!=None:
            temp=self.head
            self.head=node
            node.next=temp
        else: self.head=node

    def insertAfter(self,prev_node_value,new_node):
        temp=self.head
        while(temp):
            if temp.data is prev_node_value:
                new_node.next=temp.next
                temp.next=new_node
                break;
            else:
                temp=temp.next

        

if __name__ == "__main__":
   
    #initializing the linkList
    linkList =LinkList()

    # #creating the Nodes
    first=Node("1")
    second=Node("2")
    third=Node("3")
    forth=Node("4")

    # #INSERT IN LAST LINK LIST
    linkList.head=first
    first.next=second
    second.next=third
    third.next=forth

    ###INSERT IN BEGNING LINK LIST

    # linkList.insertInBegnning(first)
    # linkList.insertInBegnning(second)
    # linkList.insertInBegnning(third)
    # linkList.insertInBegnning(forth)

    ###INSERT AT DEFINED LOCATION

    # linkList.printLinkList()
    # new_node=Node("10")
    # linkList.insertAfter("4", new_node)
    # print()
    # linkList.printLinkList()
    
    #printing the nodes
  




    