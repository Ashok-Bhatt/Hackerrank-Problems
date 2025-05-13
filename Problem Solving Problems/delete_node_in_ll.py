

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    
    previous = None
    current = llist
    
    for i in range(position):
        previous = current
        current = current.next
    
    if previous is None:
        nextNode = current.next
        current.next = None
        del current
        return nextNode
    else:
        nextNode = current.next
        previous.next = nextNode
        current.next = None
        del current
        return llist

