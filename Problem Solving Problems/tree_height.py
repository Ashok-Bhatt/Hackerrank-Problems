

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def getHeight(root):
    if root is None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1

def height(root):
    return getHeight(root) - 1

