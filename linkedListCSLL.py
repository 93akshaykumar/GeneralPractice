class Node:
    def __init__(self):
        self.value=input('Please Enter The value to Enter in Node==')
        self.next=None
        
class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

def linkedListInsert(linkList):
    if linkList.head==None:
        node= Node()
        linkList.head=node
        node.next=linkList.head
        linkList.count+=1
    else:
        place=input('Please Enter the Specific location where you want to enter the value(s for begining,e for end, [1-n])')
        if place=='s':
            node=Node()
            node.next=linkList.head
            linkList.head=node
            linkList.count+=1
        elif place=='e':
            newNode=Node()
            node=linkList.tail
            newNode.next=linkList.head
            node.next=newNode
            linkList.count+=1
        else:
            newNode=Node()
            place=int(place)
            node=linkList.head
            for i in range(1,place-1):
                if node is None:
                    print("Trying to Enter value out of bound")
                    break
                else:
                    node=node.next
            newNode.next=node.next
            node.next=newNode
            linkList.count+=1
            
                

def linkedListSearch(linkList):
    find=input('Enter The Number you want to search----')
    node=linkList.head
    check=False
    counter+=1
    for n in range(linkList.count):
        if node.value == find:
            check=True
            break
        else:
            counter+=1
            node=node.next
    if check==True:
        print('Value is present')
    else:
        print('The Value is not present')
    
    
def linkedListPrint(linkList):
    if linkList.head==None:
        print('Link List is fully Empty')
    else:
        node=linkList.head
        print("Hello---",linkList.count)
        for n in range(linkList.count+10):
            print(n+1,"-----",node.value)
            node=node.next
            


def linkedListDelete(linkList):
    counter=1
    if linkList.head==None:
        print('List is empty.Nothing to Delete')
    else:
        find=input('Enter The Number you want to delete----')
        node=linkList.head
        check=False
        while node is not None:
            if node.value == find:
                check=True
                break
            else:
                counter+=1
                prevNode=node
                node=node.next
        if check==True:
            if counter==1:
                linkList.head=node.next
            elif node.next is None:
                prevNode.next=node.next
                linkList.tail=prevNode.next
            else:
                prevNode.next=node.next

            if linkList.head is None:
                linkList.tail==None           
            print('deletion Done')
        else:
            print('The Value is not present')
                        
            
    

choice=''
linkList= SlinkedList()
while choice!=5:
    print('1.insert a Node')
    print('2.search a Node')
    print('3.print the whole Linked List')
    print('4.delete a Node')
    print('5. exit')
    choice=int(input("Pleae Enter The choise from below Menu to perform on Linked List=="))
    if choice==1: linkedListInsert(linkList)
    elif choice==2: linkedListSearch(linkList)
    elif choice==3: linkedListPrint(linkList)
    elif choice==4: linkedListDelete(linkList)
    else: break

