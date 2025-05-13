

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    
    current = llist
    previous = None
    newNode = SinglyLinkedListNode(data)
    
    for i in range(position):
        previous = current
        current = current.next
    
    if (previous is None):
        newNode.next = current
        return newNode
    else:
        previous.next = newNode
        newNode.next = current
        return llist

