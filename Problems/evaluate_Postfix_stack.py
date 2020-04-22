class Stack:
    def __init__(self):
        self.top=-1
        self.stack=[]

    def push(self,data):
        self.stack.append(data)
        self.top+=1
    
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.stack.pop()
        else: return None

    def getpeek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else: return None

    def isEmpty(self):
        if self.top != -1:
            return False
        else: return True

class Evaluate:
    def __init__(self):
        self.bucket=Stack()
        
    def evalutePost(self,exp):
        for value in exp:
            if value.isdigit():
                self.bucket.push(str(value))
            else:
                v1=self.bucket.pop()
                v2=self.bucket.pop()
                self.bucket.push(str(eval (v2+value+v1)))
        return self.bucket.pop()




if __name__ == "__main__":
    obj= Evaluate()
    
    exp="55+"
    print("The Outpit is ::-->",obj.evalutePost(exp))


