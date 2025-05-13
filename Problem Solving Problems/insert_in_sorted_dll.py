

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev



def sortedInsert(llist, data):
    
    newNode = DoublyLinkedListNode(data)
    
    if llist is None:
        return newNode
    
    previous = None
    current = llist
    forward = llist.next
    
    while (current is not None) and (current.data <= data):
        previous = current
        current = forward
        if (forward is not None):
            forward = forward.next
        
    if current is None:
        previous.next = newNode
        newNode.prev = previous
    else:
        newNode.next = current
        current.prev = newNode
        newNode.prev = previous
        if previous is not None:
            previous.next = newNode
        else:
            llist = newNode
    
    return llist

