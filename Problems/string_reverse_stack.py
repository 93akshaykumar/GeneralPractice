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

class Reverse:
    def __init__(self):
        self.bucket=Stack()

    def reverse(self,exp):
        for val in exp:
            self.bucket.push(val)
        rev=""
        while self.bucket.getpeek():
            rev+=self.bucket.pop()

        return rev



if __name__ == "__main__":
    obj= Reverse()
    exp="GeeksQuiz"
    print("The Outpit is ::-->",obj.reverse(exp))


    
