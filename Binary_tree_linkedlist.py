class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def PreOrderTraversal(self,root):
        if root.data != None:
            print(root.data)
            PreOrderTravsesal(root.left())
            PreOrderTravsesal(root.right())

    def InOrderTraversal(self,root):
        if root.data != None:  
            PreOrderTravsesal(root.left())
            print(root.data)
            PreOrderTravsesal(root.right())

    def PostOrderTraversal(self,root):
        if root.data != None:  
            PreOrderTravsesal(root.left())
            PreOrderTravsesal(root.right())
            print(root.data)
        


    


root = Node(10)

root.PrintTree()

