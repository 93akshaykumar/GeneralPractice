queue=[]
def popout():
    if len(queue)<=0:
        print('The Queue is empty')
    else:
        queue.pop(0)


def pushin():
    queue.append(input('Please ENter The Number=='))

def showQueue():
    print('The element in Queue is==',queue)

choice=''
while choice!=4:
    print('1.Add to Queue')
    print('2.Remove to Queue')
    print('3.Show')
    print('4.Exit')
    choice=input('Please Enter The Choice==')
    if choice=='1': pushin()
    elif choice=='2': popout()
    elif choice=='3': showQueue()
    else: break
