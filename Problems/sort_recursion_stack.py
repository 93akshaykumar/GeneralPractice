class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1

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

class Sort:
    def __init__(self):
        self.bucket=Stack()

    def inserttoStack(self,val):
            if self.bucket.top==-1:
                self.bucket.push(val)
            elif self.bucket.getpeek()<=val:
                self.bucket.push(val)
            else:
                temp=self.bucket.pop()
                self.inserttoStack(val)
                self.bucket.push(temp)
        

    def insert(self,arr):

        for val in arr:
            self.inserttoStack(val)

        while self.bucket.top!=-1:
            print("The Value at==",self.bucket.top," == ",self.bucket.pop())



if __name__ == "__main__":
    obj=Sort()
    Exp=[-3,14,18,-5,30]
    obj.insert(Exp)