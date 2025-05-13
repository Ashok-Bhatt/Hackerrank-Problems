

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def length(node):
    
    lengthOfNode = 0
    while (node is not None):
        lengthOfNode += 1
        node = node.next
        
    return lengthOfNode

def getNode(llist, positionFromTail):
    
    position = length(llist) - positionFromTail - 1
    temp = llist
    for i in range(position):
        temp = temp.next
    
    return temp.data
    

