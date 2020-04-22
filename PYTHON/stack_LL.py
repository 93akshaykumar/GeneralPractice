class Node:
    def __init__(self):
        self.value=input('Please Enter The value to Enter in Node==')
        self.next=None
        
class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

def linkedListPush(linkList):
    if linkList.head==None:
        node= Node()
        linkList.head=node
        linkList.tail=node
    else:
            node=Node()
            node.next=linkList.head
            linkList.tail=linkList.head
            linkList.head=node

    
    
def linkedListShow(linkList):
    counter=1
    if linkList.head==None:
        print('Link List is fully Empty')
    else:
        node=linkList.head
        while node is not None:
            print(counter,"-----",node.value)
            counter+=1
            node=node.next
            


def linkedListPop(linkList):
    if linkList.head.next!=None:
        linkList.head=linkList.head.next
    else:
        linkList.head=None           
            
    

choice=''
linkList= SlinkedList()
while choice!=5:
    print('1.PUSH a Node')
    print('2.POP a Node')
    print('3.print the whole Linked List')
    print('5. exit')
    choice=int(input("Pleae Enter The choise from below Menu to perform on Linked List=="))
    if choice==1: linkedListPush(linkList)
    elif choice==2: linkedListPop(linkList)
    elif choice==3: linkedListShow(linkList)
    else: break

