#Code for Complete Binary Tree......

class Node:
    def __init__(self,value=None):
        self.data=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.head=None 

    def insertLevelOrder(self,arr, root, i, n): 

        # Base case for recursion  
        if i < n: 
            temp = Node(arr[i])  
            if self.head is None:
                self.head=temp
                root=self.head
            else:
                root = temp  

            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)  
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n) 
        return root 
         
            

    def printInorder(self,root): 
  
        if root: 
            self.printInorder(root.left) 
            print(root.data), 
            self.printInorder(root.right) 
  
  
  
    def printPostorder(self,root): 
    
        if root: 
            self.printPostorder(root.left) 
            self.printPostorder(root.right) 
            print(root.data), 
    
  
    def printPreorder(self,root): 
    
        if root:
            print(root.data), 
            self.printPreorder(root.left) 
            self.printPreorder(root.right) 

   

binayTree = BinaryTree()

arr=[]

for val in range(0,10):
    arr.append(val)

print(arr)

binayTree.insertLevelOrder(arr,None,0,10)

print("\nInorder traversal")
binayTree.printInorder(binayTree.head)
print("\nPreorder Traversal")
binayTree.printPreorder(binayTree.head)
print("\nPost order traversal")
binayTree.printPostorder(binayTree.head)