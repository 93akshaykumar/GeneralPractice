
stack=[None,None,None,None,None,None]
stack=[10,20,30,40,50,60]
def pushIn():
    value=int(input('Please ENter The value=='))
    if stack[5]!=None:
        return 'Error!! Stack is Full.Please POP something'
    else:
        temp=None
        for n in range(6):
            if stack[n]!=None or temp!=None:
                temp,stack[n]=stack[n],temp
            else:
                break
        stack[0]=value
        return True

def popOut():
    
    if stack[0]==None:
        return 'Error!! Stack is Empty.Please PUSH something'
    else:
        for n in range(0,6):
            if n==5:
                stack[5]=None
            else:
                if stack[n+1]!=None:
                    stack[n]=stack[n+1]
                    stack[n+1]=None
                else:
                    break
            
        return True
            
def showAll():
    if stack[0]==None:
        return 'Error!! Stack is Empty.Please PUSH something'
    else:             
        return stack
choice=''
while choice!=4:        
    print('1. PUSH')
    print('2. POP')
    print('3. SHOW')
    print('4. EXIT')
    choice=int(input('Enter The action you want to perform in python'))
    if choice==1:
        print('The Element is pushed==',pushIn())
    if choice==2:
        print('The Element is poped==',popOut())
    if choice==3:
        print('The Element is STACk==',showAll())
