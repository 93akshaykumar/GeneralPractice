# This Is the program to convert the infix expression to Postfix expression using stack
# Example:
#     INPUT = a+b*(c^d-e)^(f+g*h)-i
#     OUTPUT = abcd^e-fgh*+^*+i-



class Change:
    def __init__(self):
        self.stack=[]
        self.output=[]
        self.top=-1
        self.order={'+':1, '-':1, '*':2, '/':2, '^':3}

    def push(self,val):
        self.top+=1
        self.stack.append(val)

    def isEmpty(self):
        if self.top==-1:
            return True
        else: return False

    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.stack.pop()
        else:
            return None
    def isoperand(self,val):
        if val.isalpha(): return True
        else: False
    
    def getpeek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else: return None
    
    def inorder(self,op):
        
        ext=self.getpeek()
        #print("inorder::",ext)
        if self.order.get(op,0)>self.order.get(ext,0): 
            return True
        else: False

    def write(self):
        result=str("".join(self.output))
        #print("resss::",result)
        while self.top!=-1:
            result=result+("".join(self.pop()))
        return result

    def infixToPostfix(self,exp=""):
        for val in exp:
            #print('val::--> ',val)
            if self.isoperand(val):
                self.output.append(val)
            elif val is '(':
                self.push(val)
            elif val is ')':
                while self.getpeek()!='(' and not self.isEmpty():
                    self.output.append(self.pop())
                else:
                    self.pop()
            else:
                #print('OP::--> ',val)
                while (not self.isEmpty()) and (not self.inorder(val)):
                    self.output.append(self.pop())
                else:
                    self.push(val) 
        
        return self.write()
                
if __name__ == "__main__":
    obj=Change()
    exp="a+b*(c^d-e)^(f+g*h)-i"
    print("The Outpit is ::-->",obj.infixToPostfix(exp))



