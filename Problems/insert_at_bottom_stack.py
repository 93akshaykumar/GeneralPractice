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


class Insert:
    def __init__(self):
        self.bucket=Stack()

    def inserttoBottom(self,val):
        if self.bucket.top==-1:
            self.bucket.push(val)
        else:
            temp=self.bucket.pop()
            self.inserttoBottom(val)
            self.bucket.push(temp)
        

    def insert(self,arr):

        for val in arr:
            self.inserttoBottom(val)

        print("The element at top of the Bucket::",self.bucket.getpeek())


if __name__ == "__main__":
    obj=Insert()
    Exp=[1,2,3,4,5]
    obj.insert(Exp)